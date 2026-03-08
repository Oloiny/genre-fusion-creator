#!/usr/bin/env python3
# config.py - 配置管理和验证

"""
配置管理模块

功能：
- 加载环境变量
- 验证配置有效性
- 提供默认配置
"""

import os
from pathlib import Path
from typing import Optional

# dotenv 是可选依赖，没有安装时也能运行
try:
    from dotenv import load_dotenv
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


class ConfigError(Exception):
    """配置错误"""
    pass


class Config:
    """配置管理器"""
    
    def __init__(self):
        """初始化配置"""
        # 加载 .env 文件
        env_path = Path(__file__).parent.parent / ".env"
        if env_path.exists():
            if DOTENV_AVAILABLE:
                load_dotenv(env_path)
            else:
                # 手动解析 .env 文件（简单版本）
                self._parse_env_file(env_path)
        
        # 从环境变量加载配置
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.model = os.getenv("MODEL", "dashscope-coding/qwen3.5-plus")
        self.debug = os.getenv("DEBUG", "false").lower() == "true"
    
    def _parse_env_file(self, env_path: Path):
        """
        手动解析 .env 文件（当 python-dotenv 不可用时）
        
        只支持简单的 KEY=VALUE 格式
        """
        try:
            content = env_path.read_text(encoding="utf-8")
            for line in content.splitlines():
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    key = key.strip()
                    value = value.strip().strip('"').strip("'")
                    os.environ[key] = value
        except Exception as e:
            print(f"⚠️  解析 .env 文件失败：{e}")
    
    def validate(self, strict: bool = False) -> bool:
        """
        验证配置
        
        Args:
            strict: 是否严格模式（严格模式下 API Key 缺失会抛异常）
            
        Returns:
            配置是否有效
            
        Raises:
            ConfigError: 严格模式下 API Key 缺失
        """
        if not self.api_key:
            if strict:
                raise ConfigError(
                    "API Key 未配置！\n"
                    "请设置环境变量 DASHSCOPE_API_KEY\n"
                    "或创建 .env 文件，内容：DASHSCOPE_API_KEY=your_key_here"
                )
            return False
        
        # 验证 API Key 格式（DashScope 的 key 通常是 sk- 开头）
        if not self.api_key.startswith("sk-"):
            if strict:
                print("⚠️  警告：API Key 格式可能不正确（DashScope Key 通常以 sk- 开头）")
            # 不抛异常，让用户自己决定
        
        return True
    
    def get_api_key(self) -> Optional[str]:
        """获取 API Key"""
        return self.api_key
    
    def get_model(self) -> str:
        """获取模型名称"""
        return self.model
    
    def is_debug(self) -> bool:
        """是否调试模式"""
        return self.debug
    
    def to_dict(self) -> dict:
        """转换为字典（用于日志）"""
        return {
            "api_key_configured": bool(self.api_key),
            "model": self.model,
            "debug": self.debug,
        }


# 全局配置实例
_global_config: Optional[Config] = None


def get_config() -> Config:
    """获取全局配置实例"""
    global _global_config
    if _global_config is None:
        _global_config = Config()
    return _global_config


def validate_config(strict: bool = False) -> bool:
    """
    验证全局配置
    
    Args:
        strict: 是否严格模式
        
    Returns:
        配置是否有效
    """
    return get_config().validate(strict)


def check_api_key() -> bool:
    """
    检查 API Key 是否配置
    
    Returns:
        是否已配置
    """
    config = get_config()
    return bool(config.api_key)
