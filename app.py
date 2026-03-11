import streamlit as st
from resume_parser import extract_resume_text
from ai_matcher import calculate_similarity
from matcher import match_skills

st.title("AI Resume Screening System")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file:

    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_resume_text("resume.pdf")

    with open("skills.txt") as f:
        skills = [s.strip() for s in f.readlines()]

    score, matched, missing = match_skills(resume_text, skills)

    st.subheader(f"Match Score: {score:.2f}%")
