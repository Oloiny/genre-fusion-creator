# 使用指南

快速上手类型融合创新器。

---

## 🚀 快速开始

### 1. 安装依赖

```bash
# 进入项目目录
cd genre-fusion-creator

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置 API Key

**方式 A：环境变量**
```bash
export DASHSCOPE_API_KEY=your_api_key_here
```

**方式 B：.env 文件**
```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env，填入你的 API Key
# 获取 API Key: https://dashscope.console.aliyun.com/apiKey
```

### 3. 运行

#### CLI 模式

```bash
# 基础用法
python src/fusion_engine.py "Roguelike" "模拟经营"

# 三个类型融合
python src/fusion_engine.py "RPG" "竞速" "社交模拟"

# 添加约束
python src/fusion_engine.py "解谜" "恐怖" --constraint "platform:移动端"

# 生成 3 个方案
python src/fusion_engine.py "RTS" "恋爱模拟" --multi

# 保存到文件
python src/fusion_engine.py "Roguelike" "模拟经营" -o my_design.md
```

#### Web 界面模式

```bash
# 启动 Web 服务
python src/web_ui.py

# 访问 http://localhost:7860
```

---

## 📋 输出格式

每个融合方案包含：

```markdown
## 融合方案：[类型 A] × [类型 B]

### 🎯 核心概念
一句话描述游戏的核心体验

### 🔄 核心循环
- 短期循环（每局/每分钟）
- 中期循环（每局/每小时）
- 长期循环（Meta 进度）

### 🔗 关键机制融合
| 类型 A 元素 | 类型 B 元素 | 融合方式 | 设计意图 |
|------------|------------|---------|---------|
| ...        | ...        | ...     | ...     |

### ✨ 创新点
1. **创新点名称**：详细描述
2. ...

### ⚠️ 潜在风险
- 机制冲突
- 认知负担
- 开发复杂度

### 📚 参考案例
- 类似融合的成功游戏

### 🎲 变体建议
- 简化版
- 激进版
- 商业化版
```

---

## 💡 使用场景

### 游戏设计师
快速生成创意原型，用于：
- 头脑风暴
- 设计文档初稿
- 团队讨论基础

### Game Jam 参赛者
寻找独特的融合主题：
```bash
python src/fusion_engine.py "2D 平台" "卡牌" "roguelike" --multi
```

### 独立开发者
探索蓝海市场：
```bash
python src/fusion_engine.py "模拟经营" "FPS" --constraint "scope:独立小品"
```

### 学生/研究者
研究游戏类型演化：
```bash
# 批量生成（需要自己写脚本）
for genre1 in "RPG" "ACT" "AVG"; do
  for genre2 in "竞速" "解谜" "恐怖"; do
    python src/fusion_engine.py "$genre1" "$genre2" -o "output/${genre1}_${genre2}.md"
  done
done
```

---

## ⚙️ 高级用法

### 自定义模型

编辑 `src/fusion_engine.py`，修改默认模型：
```python
self.model = model or "dashscope/qwen-max"
```

### 批量生成

创建脚本 `batch_generate.py`：
```python
from fusion_engine import FusionEngine

engine = FusionEngine()

pairs = [
    ("Roguelike", "模拟经营"),
    ("RPG", "竞速"),
    ("解谜", "恐怖"),
]

for g1, g2 in pairs:
    result = engine.generate_fusion([g1, g2])
    with open(f"examples/{g1}_{g2}.md", "w") as f:
        f.write(result)
```

### 集成到你的项目

```python
from src.fusion_engine import FusionEngine

engine = FusionEngine(api_key="your_key")
scheme = engine.generate_fusion(
    genres=["RPG", "模拟经营"],
    constraints="platform:移动端",
)
print(scheme)
```

---

## 🔧 故障排除

### 问题：提示 "未检测到 API Key"

**解决**：
```bash
# 检查环境变量
echo $DASHSCOPE_API_KEY

# 如果为空，设置它
export DASHSCOPE_API_KEY=your_key_here
```

### 问题：提示 "未安装 dashscope 库"

**解决**：
```bash
pip install dashscope
```

### 问题：输出质量不高

**建议**：
1. 尝试添加约束条件，如 `scope:独立小品`
2. 使用 `--multi` 生成多个方案，选最好的
3. 手动调整提示词模板（`src/prompts.py`）

---

## 📚 更多资源

- [设计原则](design_principles.md) - 融合设计理念
- [示例方案](../examples/) - 参考输出
- [GitHub 仓库](https://github.com/yourusername/genre-fusion-creator) - 项目主页

---

**有问题？** 提 Issue 或联系作者。
