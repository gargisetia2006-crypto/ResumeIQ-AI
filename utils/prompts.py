# SYSTEM PROMPT
SYSTEM_PROMPT = """
You are an expert ATS (Applicant Tracking System) Resume Reviewer.
Your responsibilities are:
- Analyze resumes professionally and objectively.
- Evaluate the resume according to the selected job role.
- Never invent skills, experience, certifications, or projects.
- If information is missing, clearly state that it is missing.
- Give constructive and actionable suggestions.
- Be concise and factual.
- Return only the requested information.
"""

# USER PROMPT
def build_prompt(resume_text, job_role):
    """
    Creates a dynamic prompt using
    the uploaded resume and selected job role.
    """

    prompt = f"""
Analyze the following resume for the role of:
{job_role}
RESUME
{resume_text}
TASK
Evaluate this resume carefully.
Return the following:

1. ATS Score (integer only)
2. Top 5 strengths (maximum 5 bullet points)
3. Top 8 missing skills
4. Top 8 missing keywords
5. Top 5 resume improvements
6. Top 3 recommended projects
7. Top 3 recommended certifications
9. Summary (maximum 100 words)

Keep every response concise.
Do not invent any information that is not present in the resume.
Base your evaluation on the selected job role.
"""

    return prompt