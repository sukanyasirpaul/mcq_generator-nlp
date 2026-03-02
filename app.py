import streamlit as st
from mcq_logic import generate_mcqs

st.set_page_config(page_title="Automated MCQ Generator")

st.title("📘 Automated MCQ Generator using NLP")
st.write("Generate MCQs from text or upload file")

# Text input
text_input = st.text_area("Enter paragraph here:")

# TXT file upload
uploaded_file = st.file_uploader("Or upload a .txt file", type=["txt"])

num_questions = st.slider("Number of MCQs", 1, 10, 3)

if st.button("Generate MCQs"):

    if uploaded_file is not None:
        text = uploaded_file.read().decode("utf-8")
    else:
        text = text_input

    if text.strip() != "":
        mcqs = generate_mcqs(text, num_questions)

        if mcqs:
            for i, mcq in enumerate(mcqs):
                st.subheader(f"Question {i+1}")
                st.write(mcq["question"])

                for option in mcq["options"]:
                    st.write(f"- {option}")

                st.success(f"Correct Answer: {mcq['answer']}")
        else:
            st.error("Not enough content to generate MCQs.")
    else:
        st.warning("Please enter text or upload a file.")
