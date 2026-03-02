import spacy
import random

    nlp = spacy.load("en_core_web_sm")

def generate_mcqs(text, num_questions=3):
    doc = nlp(text)
    sentences = list(doc.sents)

    mcqs = []

    for sent in sentences:
        words = [token.text for token in sent 
                 if token.pos_ in ["NOUN", "PROPN"] and len(token.text) > 3]

        if len(words) >= 4:
            answer = random.choice(words)
            question_text = sent.text.replace(answer, "______")

            options = random.sample(words, 4)
            random.shuffle(options)

            mcqs.append({
                "question": question_text,
                "options": options,
                "answer": answer
            })

        if len(mcqs) == num_questions:
            break


    return mcqs

