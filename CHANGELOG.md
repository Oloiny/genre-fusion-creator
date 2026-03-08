# 更新日志 (CHANGELOG)

所有重要更新将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

---

## [0.1.0-alpha] - 2026-03-08

### ✨ 新增

- **核心功能**
  - CLI 命令行工具，支持 2-3 个类型融合
  - Web 界面（Gradio），图形化操作
  - 多方案生成（保守/平衡/激进）
  - 约束条件支持（platform、scope、audience 等）

- **提示词工程**
  - 系统提示词：4 维度分析框架（核心循环、玩家目标、反馈节奏、创新点）
  - Few-shot 示例：引导高质量输出
  - 结构化输出模板：核心概念、核心循环、机制融合、创新点、风险、案例、变体
  - 评估提示词：5 维度评分（创新性、可行性、趣味性、市场潜力、融合深度）

- **配置管理**
  - 环境变量支持（DASHSCOPE_API_KEY）
  - .env 文件配置
  - 配置验证（`--check-config`）

- **文档**
  - README.md：英文项目说明（默认）
  - README_zh.md：中文项目说明
  - USAGE.md：详细使用指南
  - design_principles.md：融合设计原则
  - 5 个完整示例方案

- **工程化**
  - 版本管理（`__version__.py`）
  - 测试套件（pytest）
  - .gitignore 配置
  - MIT 许可证

- **国际化**
  - 中英双语 README
  - 语言切换链接

### 📝 示例方案

- `roguelike_sim_social.md` - Roguelike × 模拟经营 × 社交模拟
- `rpg_racing.md` - RPG × 竞速
- `puzzle_horror.md` - 解谜 × 恐怖
- `rts_dating.md` - RTS × 恋爱模拟

### ⚠️ 已知限制

- Web 界面为实验性功能，未经过充分测试
- 评估功能（`--evaluate`）需要真实 API Key 才能工作
- Mock 模式下只返回固定示例，不响应输入

### 🔮 计划中

- [ ] 批量生成工具
- [ ] 导出格式支持（PDF、JSON）
- [ ] 迭代优化循环（生成→评估→改进）
- [ ] 更多 Few-shot 示例
- [ ] Web 界面完善
- [ ] GitHub Actions 自动测试

---

## 版本说明

### v0.1.0-alpha (2026-03-08)

**首个公开测试版**

适合人群：
- 游戏设计师想快速生成创意原型
- Game Jam 参赛者寻找独特主题
- 独立开发者探索蓝海市场
- 研究者研究游戏类型融合

**状态**：核心功能可用，提示词工程和输出质量还在持续优化中。

---

## 贡献

欢迎贡献！可以：

- 提交新的融合示例
- 改进提示词模板
- 报告 Bug 或提出建议
- 完善文档

详见 [CONTRIBUTING.md](CONTRIBUTING.md)（待创建）
