#!/usr/bin/env python3
# web_ui.py - 类型融合创新器 Web 界面

"""
使用 Gradio 构建简单的 Web 界面

运行：python web_ui.py
访问：http://localhost:7860

注意：需要先安装 gradio
pip install gradio
"""

from pathlib import Path
import sys

# 添加 src 目录到路径
sys.path.insert(0, str(Path(__file__).parent))

# 检查 gradio 是否安装
try:
    import gradio as gr
    GRADIO_AVAILABLE = True
except ImportError:
    GRADIO_AVAILABLE = False
    print("❌ 未安装 gradio")
    print("   运行：pip install gradio")
    print("   或：pip install -r requirements.txt")
    sys.exit(1)

from fusion_engine import FusionEngine


def generate_fusion(genre1, genre2, genre3, constraint, multi_scheme):
    """生成融合方案"""
    genres = [g.strip() for g in [genre1, genre2] if g.strip()]
    if genre3.strip():
        genres.append(genre3.strip())
    
    if len(genres) < 2:
        return "❌ 请至少输入 2 个游戏类型"
    
    engine = FusionEngine()
    
    try:
        result = engine.generate_fusion(
            genres=genres,
            constraints=constraint.strip() if constraint else "",
            multi_scheme=multi_scheme,
        )
        return result
    except Exception as e:
        return f"❌ 生成失败：{e}"


def create_demo():
    """创建 Gradio 界面"""
    with gr.Blocks(title="类型融合创新器", theme=gr.themes.Soft()) as demo:
        gr.Markdown("""
        # 🎮 类型融合创新器
        
        输入 2-3 个游戏类型，生成深度融合的设计方案。
        
        **示例**：Roguelike + 模拟经营 + 社交模拟
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("### 输入")
                genre1 = gr.Textbox(label="类型 1", placeholder="如：Roguelike", value="Roguelike")
                genre2 = gr.Textbox(label="类型 2", placeholder="如：模拟经营", value="模拟经营")
                genre3 = gr.Textbox(label="类型 3（可选）", placeholder="如：社交模拟", value="社交模拟")
                constraint = gr.Textbox(label="约束条件（可选）", placeholder="如：platform:移动端，scope:独立小品")
                multi_scheme = gr.Checkbox(label="生成 3 个方案（保守/平衡/激进）", value=False)
                
                generate_btn = gr.Button("🚀 生成方案", variant="primary")
            
            with gr.Column(scale=2):
                gr.Markdown("### 输出")
                output = gr.Textbox(label="融合方案", lines=30, show_copy_button=True)
        
        # 示例按钮
        gr.Markdown("### 快速示例")
        with gr.Row():
            example1 = gr.Button("RPG × 竞速")
            example2 = gr.Button("解谜 × 恐怖")
            example3 = gr.Button("RTS × 恋爱模拟")
        
        # 示例事件
        example1.click(
            fn=lambda: ("RPG", "竞速", "", "", False),
            outputs=[genre1, genre2, genre3, constraint, multi_scheme]
        )
        example2.click(
            fn=lambda: ("解谜", "恐怖", "", "", False),
            outputs=[genre1, genre2, genre3, constraint, multi_scheme]
        )
        example3.click(
            fn=lambda: ("RTS", "恋爱模拟", "", "", False),
            outputs=[genre1, genre2, genre3, constraint, multi_scheme]
        )
        
        # 生成事件
        generate_btn.click(
            fn=generate_fusion,
            inputs=[genre1, genre2, genre3, constraint, multi_scheme],
            outputs=output,
        )
        
        gr.Markdown("""
        ---
        **Made with ❤️ by Genre Fusion Creator** | 
        [GitHub](https://github.com/yourusername/genre-fusion-creator)
        """)
    
    return demo


if __name__ == "__main__":
    demo = create_demo()
    demo.launch(server_name="0.0.0.0", server_port=7860)
