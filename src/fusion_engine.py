#!/usr/bin/env python3
# fusion_engine.py - 类型融合创新器核心引擎

"""
Genre Fusion Creator - 核心引擎

使用方法:
    python fusion_engine.py "Roguelike" "模拟经营" "社交模拟"
    
或者添加约束:
    python fusion_engine.py "RPG" "竞速" --constraint "platform:移动端"

环境配置:
    设置 DASHSCOPE_API_KEY 环境变量，或在 .env 文件中配置
"""

import sys
import os
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, List

# 导入提示词模板
from prompts import (
    FUSION_SYSTEM_PROMPT,
    FUSION_USER_TEMPLATE,
    MULTI_SCHEME_PROMPT,
    EVALUATION_PROMPT,
    parse_constraints,
)

# 导入配置和版本
from config import get_config, check_api_key, ConfigError
from __version__ import __version__


class FusionEngine:
    """类型融合引擎"""

    def __init__(self, api_key: Optional[str] = None, model: str = None):
        """
        初始化引擎
        
        Args:
            api_key: LLM API 密钥（可选，优先使用环境变量 DASHSCOPE_API_KEY）
            model: 使用的模型名称
        """
        # 优先使用传入的 api_key，其次使用全局配置
        self.api_key = api_key or get_config().get_api_key()
        self.model = model or get_config().get_model()
        self.output_dir = Path(__file__).parent.parent / "examples"
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # 检查 API key 是否配置
        if not self.api_key:
            print("⚠️  警告：未检测到 API Key")
            print("   请设置环境变量 DASHSCOPE_API_KEY")
            print("   或创建 .env 文件，内容：DASHSCOPE_API_KEY=your_key_here")
            print("   将使用示例输出（mock 模式）\n")

    def generate_fusion(self, genres: List[str], constraints: str = "", multi_scheme: bool = False) -> str:
        """
        生成类型融合方案
        
        Args:
            genres: 游戏类型列表，如 ["Roguelike", "模拟经营"]
            constraints: 可选约束条件（如 "platform:移动端，scope:独立小品"）
            multi_scheme: 是否生成多个方案
            
        Returns:
            生成的融合方案（Markdown 格式）
        """
        # 构建提示词
        genre_names = " × ".join(genres)
        
        # 解析约束条件
        parsed_constraints = parse_constraints(constraints)
        
        if multi_scheme:
            prompt = MULTI_SCHEME_PROMPT.format(
                genres=", ".join(genres),
            )
        else:
            prompt = FUSION_USER_TEMPLATE.format(
                genres=", ".join(genres),
                constraints=parsed_constraints,
                genre_names=genre_names,
                genre_a=genres[0] if len(genres) >= 1 else "类型 A",
                genre_b=genres[1] if len(genres) >= 2 else "类型 B",
            )

        # 调用 LLM
        response = self._call_llm(
            system_prompt=FUSION_SYSTEM_PROMPT,
            user_prompt=prompt,
        )

        return response
    
    def evaluate(self, scheme_content: str) -> str:
        """
        评估融合方案
        
        Args:
            scheme_content: 方案内容
            
        Returns:
            评估结果（Markdown 格式）
        """
        prompt = EVALUATION_PROMPT.format(
            scheme_content=scheme_content,
        )
        
        response = self._call_llm(
            system_prompt="你是一位资深游戏设计师和评论家，擅长评估游戏设计方案的优劣。",
            user_prompt=prompt,
        )
        
        return response

    def _call_llm(self, system_prompt: str, user_prompt: str) -> str:
        """
        调用 LLM API
        
        使用 DashScope API 进行真实调用
        如果没有 API key，返回 mock 响应
        """
        if not self.api_key:
            return self._mock_response()
        
        try:
            # 尝试导入 dashscope
            import dashscope
            from dashscope import Generation
            
            response = Generation.call(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                api_key=self.api_key,
            )
            
            if response.status_code == 200:
                return response.output.text
            else:
                print(f"⚠️  API 调用失败：{response.code} - {response.message}")
                print("   将使用示例输出（mock 模式）\n")
                return self._mock_response()
                
        except ImportError:
            print("⚠️  未安装 dashscope 库")
            print("   运行：pip install dashscope")
            print("   将使用示例输出（mock 模式）\n")
            return self._mock_response()
        except Exception as e:
            print(f"⚠️  API 调用异常：{e}")
            print("   将使用示例输出（mock 模式）\n")
            return self._mock_response()

    def _mock_response(self) -> str:
        """模拟响应（用于测试）"""
        return """## 融合方案：Roguelike × 模拟经营 × 社交模拟

### 🎯 核心概念
在随机生成的末日世界中经营避难所，管理幸存者社群。每次失败后，新一代幸存者会继承部分记忆和资源，但人际关系网会重置。

### 🔄 核心循环

**短期循环**（每分钟）：
- 分配幸存者进行探索、建设、研究
- 处理突发事件（资源短缺、冲突、疾病）
- 与幸存者互动，建立关系

**中期循环**（每局）：
- 探索新区域，解锁新资源和技术
- 扩大避难所规模，接纳新幸存者
- 应对季节性挑战（寒冬、辐射风暴等）

**长期循环**（Meta 进度）：
- 代际传承：每代幸存者死亡后，下一代继承部分科技和资源
- 记忆碎片：收集前代的记忆，解锁特殊剧情
- 文明重建进度：从生存到复兴的长期目标

### 🔗 关键机制融合

| Roguelike 元素 | 模拟经营元素 | 社交模拟元素 | 融合方式 |
|---------------|-------------|-------------|---------|
| 永久死亡 | 基地建设 | 人际关系 | 代际传承：基地保留，关系重置 |
| 随机生成 | 资源管理 | 性格特质 | 每代幸存者随机生成，带不同特质 |
| 局外成长 | 科技树 | 声誉系统 | 记忆碎片解锁跨代科技和剧情 |
| 高风险决策 | 长期规划 | 群体动态 | 决策影响多代人，形成"家族传说" |

### ✨ 创新点

1. **动态家族史**：每个避难所都有独特的多代历史，自动生成"家族传说"叙事

2. **记忆继承系统**：不是简单的数值继承，而是前代的经历会影响后代的能力和剧情选项

3. **社交网络演化**：人际关系虽然每代重置，但"文化传统"会保留（如某代形成的仪式、禁忌）

4. **末日编年史**：游戏自动生成你这段文明的编年史，可导出分享

### ⚠️ 潜在风险

- **机制冲突**：Roguelike 的"快节奏失败"与模拟经营的"慢节奏建设"可能产生挫败感
- **认知负担**：玩家需要同时管理资源、关系、科技树，可能过于复杂
- **开发复杂度**：代际传承系统和动态叙事生成需要大量内容和逻辑
- **市场定位**：核心向设计，可能不适合休闲玩家

### 📚 参考案例

- 《暗黑地牢》：压力系统 + 代际继承的简化版
- 《环世界》：殖民地模拟 + 叙事生成
- 《Frostpunk》：末日生存 + 道德抉择
- 《Crusader Kings》：代际传承 + 关系网络（但这是策略游戏）

### 🎲 变体建议

- **简化版**：去掉社交模拟，专注 Roguelike + 经营（类似《暗黑地牢》）
- **激进版**：加入"时间旅行"机制，可以与前代幸存者跨时空互动
- **商业化版**：改为章节制，每代是一个章节，降低失败惩罚"""

    def save_example(self, content: str, filename: Optional[str] = None) -> Path:
        """
        保存示例到 examples 目录
        
        Args:
            content: 方案内容
            filename: 文件名（可选，自动生成）
            
        Returns:
            保存的文件路径
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"fusion_{timestamp}.md"

        filepath = self.output_dir / filename
        filepath.write_text(content, encoding="utf-8")
        return filepath


def main():
    """命令行入口"""
    parser = argparse.ArgumentParser(
        description="类型融合创新器 - 生成游戏类型融合创意",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  %(prog)s "Roguelike" "模拟经营"
  %(prog)s "RPG" "竞速" "社交模拟" --multi
  %(prog)s "解谜" "恐怖" --constraint "platform:移动端"
        """
    )

    parser.add_argument(
        "genres",
        nargs="+",
        help="要融合的游戏类型（至少 2 个）"
    )

    parser.add_argument(
        "--constraint", "-c",
        dest="constraint",
        default="",
        help="约束条件，如 'platform:移动端' 或 'scope:独立小品'"
    )

    parser.add_argument(
        "--multi", "-m",
        action="store_true",
        help="生成 3 个不同方向的方案（保守/平衡/激进）"
    )

    parser.add_argument(
        "--output", "-o",
        dest="output",
        help="输出文件路径（默认打印到终端）"
    )

    parser.add_argument(
        "--api-key",
        dest="api_key",
        help="LLM API 密钥（也可使用环境变量）"
    )

    parser.add_argument(
        "--model",
        dest="model",
        default=None,
        help="使用的模型名称（默认：dashscope-coding/qwen3.5-plus）"
    )

    parser.add_argument(
        "--version", "-v",
        action="version",
        version=f"Genre Fusion Creator {__version__}"
    )

    parser.add_argument(
        "--check-config",
        action="store_true",
        help="检查配置并退出"
    )

    parser.add_argument(
        "--evaluate", "-e",
        dest="evaluate_file",
        help="评估已有的方案文件"
    )

    # 特殊处理：--check-config 不需要 genres 参数
    if "--check-config" in sys.argv or "-c" in sys.argv:
        # 重新解析，只提取 check-config
        print(f"Genre Fusion Creator v{__version__}")
        print(f"API Key 配置：{'✅ 已配置' if check_api_key() else '❌ 未配置'}")
        print(f"默认模型：{get_config().get_model()}")
        return
    
    args = parser.parse_args()

    # 评估模式
    if args.evaluate_file:
        evaluate_path = Path(args.evaluate_file)
        if not evaluate_path.exists():
            print(f"❌ 文件不存在：{evaluate_path}")
            return
        
        content = evaluate_path.read_text(encoding="utf-8")
        engine = FusionEngine(api_key=args.api_key, model=args.model)
        print(f"📊 正在评估：{evaluate_path}")
        result = engine.evaluate(content)
        print(result)
        return

    if len(args.genres) < 2:
        parser.error("至少需要 2 个游戏类型")

    # 创建引擎
    engine = FusionEngine(api_key=args.api_key, model=args.model)

    # 生成方案
    print(f"🎮 正在融合：{' × '.join(args.genres)}")
    if args.constraint:
        print(f"📌 约束条件：{args.constraint}")
    print(f"📦 版本：v{__version__}")
    print()

    result = engine.generate_fusion(
        genres=args.genres,
        constraints=args.constraint,
        multi_scheme=args.multi,
    )

    # 输出
    if args.output:
        output_path = Path(args.output)
        output_path.write_text(result, encoding="utf-8")
        print(f"✅ 方案已保存到：{output_path}")
    else:
        print(result)


if __name__ == "__main__":
    main()
