#!/usr/bin/env python3
# test_fusion.py - 类型融合创新器测试

"""
简单测试套件

运行：pytest tests/test_fusion.py -v
"""

import pytest
from pathlib import Path
import sys

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from prompts import (
    FUSION_SYSTEM_PROMPT,
    FUSION_USER_TEMPLATE,
    MULTI_SCHEME_PROMPT,
)


class TestPrompts:
    """测试提示词模板"""

    def test_system_prompt_exists(self):
        """系统提示词应该存在且非空"""
        assert FUSION_SYSTEM_PROMPT
        assert len(FUSION_SYSTEM_PROMPT) > 100

    def test_user_template_format(self):
        """用户模板应该包含必要的占位符"""
        assert "{genres}" in FUSION_USER_TEMPLATE
        assert "{constraints}" in FUSION_USER_TEMPLATE
        assert "{genre_names}" in FUSION_USER_TEMPLATE

    def test_multi_scheme_prompt(self):
        """多方案提示词应该存在"""
        assert MULTI_SCHEME_PROMPT
        assert "{genres}" in MULTI_SCHEME_PROMPT


class TestExamples:
    """测试示例文件"""

    def test_example_files_exist(self):
        """示例文件应该存在"""
        examples_dir = Path(__file__).parent.parent / "examples"
        assert examples_dir.exists()

        # 检查是否有示例文件
        example_files = list(examples_dir.glob("*.md"))
        assert len(example_files) >= 3

    def test_example_format(self):
        """示例文件应该有正确的格式"""
        examples_dir = Path(__file__).parent.parent / "examples"
        
        for example_file in examples_dir.glob("*.md"):
            content = example_file.read_text(encoding="utf-8")
            
            # 检查必要的章节
            assert "## 🎯 核心概念" in content
            assert "## 🔄 核心循环" in content
            assert "## 🔗 关键机制融合" in content
            assert "## ✨ 创新点" in content


class TestEngine:
    """测试引擎（基础测试）"""

    def test_engine_import(self):
        """引擎模块应该可以导入"""
        try:
            from fusion_engine import FusionEngine
            assert FusionEngine is not None
        except ImportError as e:
            pytest.fail(f"无法导入 FusionEngine: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
