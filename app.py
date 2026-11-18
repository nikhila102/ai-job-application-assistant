import streamlit as st

st.title("AI Job Application Assistant")

role = st.text_input("Target job title", value="AI Engineer")
region = st.text_input("Preferred region", value="United States")
work_mode = st.selectbox("Work mode", ["Remote", "Hybrid", "On-site"])

if st.button("Preview my preferences"):
    st.write("Target role:", role)
    st.write("Preferred region:", region)
    st.write("Work mode:", work_mode)

st.subheader("Tell me about your experience")

experience = st.text_area(
    "Describe your experience in your own words",
    placeholder="I built Power BI dashboards and checked healthcare data with SQL.",
)

if st.button("Preview my experience"):
    if experience.strip():
        st.write(experience)
    else:
        st.warning("Please describe your experience first.")
        st.subheader("Job description")

job_description = st.text_area(
    "Paste the job description here",
    placeholder="Paste the responsibilities and qualifications from one job posting.",
)

if st.button("Preview job description"):
    if job_description.strip():
        st.write(job_description)
    else:
        st.warning("Paste a job description first.")
        st.subheader("Resume draft")

if st.button("Draft my resume"):
    if not experience.strip() or not job_description.strip():
        st.warning("Enter your experience and paste a job description first.")
    else:
        skill_list = [skill.strip() for skill in skills.split(",") if skill.strip()]
        job_text = job_description.lower()

        matching_skills = []
        for skill in skill_list:
            if skill.lower() in job_text:
                matching_skills.append(skill)

        st.write("**Target role:**", role)
        st.write("**Experience:**", experience)

        if industry.strip():
            st.write("**Industry:**", industry)

        if matching_skills:
            st.write("**Skills mentioned in the job posting:**", ", ".join(matching_skills))
        else:
            st.info("None of the skills you entered appeared in the job description.")