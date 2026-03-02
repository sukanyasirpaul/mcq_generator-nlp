# 📘 Automated MCQ Generator using NLP

## 🔍 Project Overview

The Automated MCQ Generator is a Natural Language Processing (NLP) based web application that automatically generates Multiple Choice Questions (MCQs) from input text.

The system leverages spaCy for linguistic analysis and Streamlit for building an interactive web interface. It extracts key concepts from text, converts them into fill-in-the-blank questions, and automatically generates plausible distractors.

This project demonstrates practical implementation of NLP techniques for educational content automation.

---

## 🚀 Live Demo

🔗 [Deployed App Link Here]

---

## 🧠 Problem Statement

Manual question paper creation is time-consuming and requires subject expertise.  
This project automates the generation of objective-type questions using NLP techniques, reducing human effort and improving scalability in educational systems.

---

## ⚙️ System Architecture

User Input (Text)
        ↓
Text Processing (spaCy NLP)
        ↓
Keyword Extraction (NOUN / PROPN)
        ↓
Question Formation (Fill in the Blank)
        ↓
Distractor Generation
        ↓
MCQ Display (Streamlit Interface)

---

## 🛠️ Technologies Used

- Python
- spaCy (NLP Processing)
- Streamlit (Web Application Framework)
- Random (Distractor Generation)
- GitHub (Version Control)
- Streamlit Cloud (Deployment)

---

## 🔬 NLP Techniques Implemented

- Tokenization
- Sentence Segmentation
- Part-of-Speech (POS) Tagging
- Keyword Extraction
- Automatic Distractor Selection

---

## 📊 Features

✔ Automatic MCQ generation  
✔ Adjustable number of questions  
✔ Interactive UI  
✔ Keyword-based distractor creation  
✔ Web-based deployment  
✔ Lightweight and scalable  

---

## ▶️ Run Locally

1. Clone repository:

git clone https://github.com/yourusername/mcq-generator-nlp.git

2. Install dependencies:

pip install -r requirements.txt

3. Run application:

python -m streamlit run app.py

---

## 🌍 Deployment

The application is deployed using Streamlit Cloud and can be accessed via the provided public link.

---

## 🎓 Academic Relevance

This project demonstrates practical implementation of Natural Language Processing in educational technology. It can be extended using transformer-based models (e.g., T5, BERT) for intelligent question generation.

---

## 🔮 Future Improvements

- Transformer-based question generation (T5)
- Difficulty level classification
- PDF upload support
- Automated scoring system
- Bloom’s Taxonomy based question levels
- Hindi / Punjabi language support

---

## 👩‍💻 Author

Sukanya Sirpaul   
Specialization: Data Science & NLP

---

## 📌 Conclusion

The Automated MCQ Generator provides a scalable and efficient solution for educational content generation using NLP techniques. It highlights the practical integration of machine learning concepts into real-world applications.
