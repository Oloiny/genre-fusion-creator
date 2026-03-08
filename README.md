# Genre Fusion Creator 🎮

**类型融合创新器** - 用 LLM 生成游戏类型融合创意的设计工具

一个帮你把 2-3 个游戏类型深度融合，产出可执行设计方案的开源工具。

> 🚧 **当前状态**: v0.1.0-alpha 测试版。核心功能可用，提示词工程和输出质量还在持续优化中。欢迎反馈和建议！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version: 0.1.0-alpha](https://img.shields.io/badge/version-0.1.0--alpha-orange.svg)](CHANGELOG.md)

---

## ✨ 特性

- 🎯 **深度分析** - 不只是简单叠加，而是机制融合
- 📋 **结构化输出** - 核心循环、机制融合表、创新点、风险评估
- 🌐 **双模式** - CLI + Web 界面，满足不同需求
- 🎨 **多方案生成** - 保守/平衡/激进三个方向可选
- 📚 **内置示例** - 4 个完整示例供参考

---

## 🚀 快速开始

### 1. 安装

```bash
git clone https://github.com/yourusername/genre-fusion-creator.git
cd genre-fusion-creator
pip install -r requirements.txt
```

### 2. 配置 API Key

```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env，填入你的 DashScope API Key
# 获取：https://dashscope.console.aliyun.com/apiKey
```

### 3. 运行

**CLI 模式**：
```bash
python src/fusion_engine.py "Roguelike" "模拟经营" "社交模拟"
```

**Web 界面**：
```bash
python src/web_ui.py
# 访问 http://localhost:7860
```

---

## 📋 输出示例

```markdown
## 融合方案：Roguelike × 模拟经营 × 社交模拟

### 🎯 核心概念
在随机生成的末日世界中经营避难所，每次失败后新一代幸存者会继承部分记忆...

### 🔄 核心循环
- 短期：探索 - 收集 - 建设循环
- 中期：幸存者关系网演化
- 长期：多代传承的文明重建

### 🔗 关键机制融合
| Roguelike 元素 | 模拟经营元素 | 融合方式 |
|---------------|-------------|---------|
| 永久死亡 | 基地建设 | 代际传承机制 |
...
```

完整示例见 [`examples/`](examples/) 目录。

---

## 📖 文档

- [**使用指南**](docs/USAGE.md) - 详细使用说明
- [**设计原则**](docs/design_principles.md) - 融合设计理念
- [**示例方案**](examples/) - 完整输出示例

---

## 🛠️ 技术架构

```
genre-fusion-creator/
├── src/
│   ├── fusion_engine.py    # 核心引擎（CLI）
│   ├── web_ui.py           # Web 界面（Gradio）
│   └── prompts.py          # LLM 提示词模板
├── examples/               # 示例输出
├── tests/                  # 测试套件
├── docs/                   # 文档
└── requirements.txt        # 依赖
```

---

## 🎮 使用场景

| 用户 | 用途 | 示例命令 |
|------|------|---------|
| **游戏设计师** | 快速生成创意原型 | `python src/fusion_engine.py "RPG" "模拟经营"` |
| **Game Jam 参赛者** | 寻找独特的融合主题 | `python src/fusion_engine.py "2D" "卡牌" --multi` |
| **独立开发者** | 探索蓝海市场 | `python src/fusion_engine.py "解谜" "恐怖" -c "scope:独立小品"` |
| **学生/研究者** | 研究游戏类型演化 | 批量生成 + 分析 |

---

## 🤝 贡献

欢迎贡献！可以：

- 提交新的融合示例
- 改进提示词模板
- 添加新功能（如评分系统、可视化）
- 报告 Bug 或提出建议

---

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

灵感来源于对游戏类型演化的研究，以及无数成功融合类型的杰作：

| 游戏 | 融合类型 |
|------|---------|
| 《暗黑地牢》 | Roguelike + 策略管理 |
| 《环世界》 | 模拟经营 + 叙事生成 |
| 《哈迪斯》 | Roguelike + 叙事驱动 |
| 《极乐迪斯科》 | RPG + 侦探模拟 |
| 《十字军之王》 | 策略 + 恋爱模拟 |
| 《Frostpunk》 | 生存 + 城市建设 |

---

**Made with ❤️ by OpenClaw** | [GitHub](https://github.com/yourusername/genre-fusion-creator)
