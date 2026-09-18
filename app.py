import streamlit as st
from google import genai


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎓",
    layout="centered"
)


# -----------------------------
# Gemini API
# -----------------------------

try:
    api_key = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(
        api_key=api_key
    )

except Exception:
    client = None


# -----------------------------
# Roadmap Generator
# -----------------------------

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

Adjust the difficulty according to the student's
current skill level.

Adjust the amount of content according to the
available learning time.

Do not overload the learner.

Use clear Markdown formatting.
"""

    response = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt
    )

    return response.output_text


# -----------------------------
# Streamlit UI
# -----------------------------

st.title("🎓 AI Learning Roadmap Generator")

st.write(
    "Create a personalized learning roadmap based on "
    "your goals, skill level, and available study time."
)

st.divider()


domain = st.text_input(
    "📚 Learning Domain",
    placeholder="e.g. Python, Web Development, Data Science"
)


level = st.selectbox(
    "📊 Skill Level",
    [
        "Beginner",
        "Intermediate",
        "Advanced"
    ]
)


learning_time = st.text_input(
    "⏳ Time to Learn",
    placeholder="e.g. 3 months, 6 months, 1 year"
)


hours_per_week = st.slider(
    "🕐 Hours Per Week",
    min_value=1,
    max_value=40,
    value=10,
    step=1
)


if st.button("🚀 Generate Roadmap"):

    if client is None:
        st.error(
            "Gemini API key is not configured. "
            "Please add GEMINI_API_KEY in Streamlit Secrets."
        )

    elif not domain:
        st.warning("Please enter a learning domain.")

    elif not learning_time:
        st.warning("Please enter your available learning time.")

    else:

        with st.spinner("🤖 Creating your personalized roadmap..."):

            try:

                roadmap = generate_roadmap(
                    domain,
                    level,
                    learning_time,
                    hours_per_week
                )

                st.success("Your roadmap is ready! 🎉")

                st.markdown(roadmap)

            except Exception as e:

                st.error(
                    f"Something went wrong: {str(e)}"
                )
