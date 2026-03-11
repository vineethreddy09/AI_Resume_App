import streamlit as st
from resume_parser import extract_resume_text
from ai_matcher import calculate_similarity
from matcher import match_skills

st.title("AI Resume Screening System")
job_desc = st.text_area("Paste Job Description")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

if uploaded_file and job_desc:

    with open("resume.pdf", "wb") as f:
        f.write(uploaded_file.read())

    resume_text = extract_resume_text("resume.pdf")

    score = calculate_similarity(resume_text, job_desc)

    st.subheader(f"AI Match Score: {score:.2f}%")

    
