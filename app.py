import streamlit as st
from mcq_logic import generate_mcqs

st.set_page_config(page_title="Automated MCQ Generator")

st.title("📘 Automated MCQ Generator using NLP")

text_input = st.text_area("Enter paragraph here:")
num_questions = st.slider("Number of MCQs", 1, 10, 3)

if st.button("Generate MCQs"):
    if text_input.strip() != "":
        mcqs = generate_mcqs(text_input, num_questions)

        if len(mcqs) > 0:
            for i, mcq in enumerate(mcqs):
                st.subheader(f"Question {i+1}")
                st.write(mcq["question"])

                for option in mcq["options"]:
                    st.write(f"- {option}")

                st.success(f"Correct Answer: {mcq['answer']}")
        else:
            st.error("Not enough content to generate MCQs.")
    else:
        st.warning("Please enter some text.")