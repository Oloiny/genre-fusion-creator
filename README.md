# Genre Fusion Creator 🎮

**LLM-powered Game Genre Fusion Design Tool**

[English](README.md) | [中文](README_zh.md)

> 🚧 **Status**: v0.2.0-alpha. New: Creative Evaluation + 20+ Case Library. Feedback welcome!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Version: 0.2.0-alpha](https://img.shields.io/badge/version-0.2.0--alpha-orange.svg)](CHANGELOG.md)

---

## ✨ Features

- 🎯 **Deep Analysis** - Not just stacking genres, but mechanism fusion
- 📋 **Structured Output** - Core loop, mechanism fusion table, innovations, risk assessment
- 📊 **Creative Evaluation** - Auto-score innovation, feasibility, market potential
- 🌐 **Dual Mode** - CLI + Web UI for different needs
- 🎨 **Multi-scheme Generation** - Conservative/Balanced/Radical options
- 📚 **Built-in Examples** - 5 examples + 20+ real game cases

---

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/Oloiny/genre-fusion-creator.git
cd genre-fusion-creator
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy example file
cp .env.example .env

# Edit .env and fill in your DashScope API Key
# Get it from: https://dashscope.console.aliyun.com/apiKey
```

### 3. Run

**CLI Mode**:
```bash
python src/fusion_engine.py "Roguelike" "Simulation" "Social"
```

**Web UI**:
```bash
python src/web_ui.py
# Visit http://localhost:7860
```

---

## 📋 Output Example

```markdown
## Fusion Scheme: Roguelike × Simulation × Social

### 🎯 Core Concept
Manage a shelter in a randomly generated post-apocalyptic world. After each failure, 
a new generation inherits partial memories and resources, but relationship networks reset.

### 🔄 Core Loop

**Short-term** (per minute):
- Assign survivors to explore, build, research
- Handle emergencies (resource shortage, conflicts, diseases)

**Mid-term** (per session):
- Explore new areas, unlock resources and technologies
- Expand shelter, accept new survivors

**Long-term** (Meta progression):
- Generational inheritance: next generation inherits tech and resources
- Memory fragments: unlock special storylines
- Civilization rebuilding progress

### 🔗 Key Mechanism Fusion

| Roguelike Element | Simulation Element | Fusion Approach |
|------------------|-------------------|-----------------|
| Permadeath | Base Building | Generational inheritance |
| Random Generation | Resource Management | Survivors with random traits |
| Meta Progression | Tech Tree | Memory fragments unlock cross-gen tech |

### ✨ Innovations

1. **Dynamic Family History**: Auto-generated "family legends" narrative
2. **Memory Inheritance System**: Past experiences affect descendant abilities
3. **Cultural Tradition Evolution**: Rituals become traditions across generations

### ⚠️ Potential Risks

- **Mechanism Conflict**: Fast-paced failure vs slow-paced building
- **Cognitive Load**: Managing resources, relationships, tech tree simultaneously
- **Development Complexity**: Generational system requires extensive content
```

Full examples in [`examples/`](examples/) directory.

---

## 📖 Documentation

- [**Usage Guide**](docs/USAGE.md) - Detailed usage instructions
- [**Design Principles**](docs/design_principles.md) - Fusion design philosophy
- [**Example Schemes**](examples/) - Complete output examples
- [**中文文档**](README_zh.md) - Chinese version

---

## 🛠️ Technical Architecture

```
genre-fusion-creator/
├── src/
│   ├── fusion_engine.py    # Core engine (CLI)
│   ├── web_ui.py           # Web UI (Gradio)
│   ├── prompts.py          # LLM prompt templates
│   ├── config.py           # Configuration management
│   └── __version__.py      # Version info
├── examples/               # Example outputs
├── tests/                  # Test suite
├── docs/                   # Documentation
└── requirements.txt        # Dependencies
```

---

## 🎮 Use Cases

| User | Purpose | Example Command |
|------|---------|-----------------|
| **Game Designers** | Rapid prototype generation | `python src/fusion_engine.py "RPG" "Simulation"` |
| **Game Jam Participants** | Find unique fusion themes | `python src/fusion_engine.py "2D" "Card" --multi` |
| **Indie Developers** | Explore blue ocean markets | `python src/fusion_engine.py "Puzzle" "Horror" -c "scope:indie"` |
| **Researchers** | Study game genre evolution | Batch generation + analysis |

---

## 🤝 Contributing

Contributions welcome! You can:

- Submit new fusion examples
- Improve prompt templates
- Add new features (scoring system, visualization)
- Report bugs or suggest improvements

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

## 🙏 Acknowledgments

Inspired by game genre evolution research and successful fusion games:

| Game | Fusion Genres |
|------|--------------|
| Darkest Dungeon | Roguelike + Strategy Management |
| RimWorld | Simulation + Narrative Generation |
| Hades | Roguelike + Narrative-driven |
| Disco Elysium | RPG + Detective Simulation |
| Crusader Kings | Strategy + Dating Sim |
| Frostpunk | Survival + City Building |

---

**Made with ❤️ by OpenClaw** | [GitHub](https://github.com/Oloiny/genre-fusion-creator)
