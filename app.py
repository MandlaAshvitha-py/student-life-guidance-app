import streamlit as st
from data import options

st.title("🎓 Student Life Guidance – MVP (10th Class)")

st.write(
    "This MVP helps students who completed 10th class "
    "to understand exams, courses, and scholarships."
)

goal = st.selectbox(
    "What are you looking for?",
    list(options.keys())
)

st.subheader("📌 Suggested Options")

for item in options[goal]:
    st.markdown(f"### {item['name']}")
    st.write(item["info"])
    st.warning(f"🔔 Alert: {item['alert']}")

st.subheader("💬 Ask a Question (Demo Chatbot)")
question = st.text_input("Type your doubt here")

if question:
    st.success(
        "This is a demo chatbot. "
        "A full AI-powered assistant will be added in future versions."
    )