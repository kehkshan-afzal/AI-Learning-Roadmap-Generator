[readme_md.md]([https://github.com/user-attachments/files/32368031/readme_md.md](https://ai-learning-roadmap-generater.streamlit.app/)
# 🎓 AI Learning Roadmap Generator

An interactive web application powered by **Google Gemini AI** and **Gradio** that creates tailored, step-by-step learning roadmaps based on a student's domain, current skill level, total target duration, and weekly available time.

---

## 📌 Features

* **Customized Learning Plans:** Generates detailed learning goals, prerequisites, weekly topics, practice exercises, projects, and tool suggestions.
* **Skill & Schedule Aware:** Automatically adapts difficulty and workload to prevent learner overload based on weekly hours and target timeframe.
* **Powered by Google GenAI:** Uses the Google GenAI SDK (`google-genai`) with Gemini models.
* **Interactive Web Interface:** Built with Gradio for a seamless UI experience.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **AI Model:** Google Gemini (`gemini-3.5-flash-lite`) via `google-genai` SDK
* **UI Framework:** [Gradio](https://www.gradio.app/)
* **Environment:** Compatible with local execution or Google Colab

---

## 🚀 Getting Started

### 1. Prerequisites & Installation

Ensure you have Python installed. Install the required packages:

```bash
pip install -q -U google-genai gradio
```

### 2. Set Up API Key

You need a **GEMINI API Key** from Google AI Studio. Set it as an environment variable in your terminal:

* **Linux/macOS:**
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```
* **Windows (Command Prompt):**
  ```cmd
  set GEMINI_API_KEY=your_api_key_here
  ```
* **Windows (PowerShell):**
  ```powershell
  $env:GEMINI_API_KEY="your_api_key_here"
  ```

If running in **Google Colab**, you can set environment variables or use Colab Secrets (`google.colab.userdata`).

---

## 📖 Usage

Run the script or notebook cells:

```python
from google import genai
import os
import gradio as gr

# Initialize Gemini Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Function to generate roadmap
def generate_roadmap(domain, level, learning_time, hours_per_week):
    prompt = f"""
You are an expert learning roadmap designer.

Create a personalized learning roadmap for a student.

Learning Domain:
{domain}

Current Skill Level:
{level}

Available Learning Time:
{learning_time}

Hours Available Per Week:
{hours_per_week}

Create a realistic and practical roadmap.

Include:
1. Learning Goal
2. Prerequisites
3. Learning Roadmap
4. Weekly Topics
5. Practice Exercises
6. Projects
7. Tools and Technologies
8. Portfolio Projects
9. Final Skills

Adjust difficulty according to skill level and amount of content according to available time.
Use clear Markdown formatting.
"""

    try:
        response = client.interactions.create(
            model="gemini-3.5-flash-lite",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Build Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🎓 AI Learning Roadmap Generator")
    gr.Markdown("### Create a personalized learning roadmap with AI")

    domain = gr.Textbox(label="📚 Learning Domain", placeholder="e.g. Python, Web Development, Data Science")
    level = gr.Dropdown(choices=["Beginner", "Intermediate", "Advanced"], value="Beginner", label="📊 Skill Level")
    learning_time = gr.Textbox(label="⏳ Time to Learn", placeholder="e.g. 3 months, 6 months, 1 year")
    hours_per_week = gr.Slider(minimum=1, maximum=40, value=10, step=1, label="🕐 Hours Per Week")

    generate_button = gr.Button("🚀 Generate Roadmap")
    output = gr.Markdown()

    generate_button.click(
        fn=generate_roadmap,
        inputs=[domain, level, learning_time, hours_per_week],
        outputs=output
    )

# Launch Application
demo.launch(share=True)
```

---

## 📸 Output Example

The app generates detailed, formatted Markdown roadmaps, including:
* **Monthly/Weekly breakdowns**
* **Actionable exercises**
* **Milestone projects**
* **Portfolio suggestions**

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
