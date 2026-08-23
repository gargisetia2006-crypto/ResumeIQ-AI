from  pydantic import BaseModel   # lets us create the blueprint  kyuki in schema we find the blueprint of output we want 
from typing import List #  a list having strings 
class ResumeAnalysis(BaseModel):   # it tells gemini that every response must be following this structure 
    ats_score: int
    strengths: List[str]
    missing_skills: List[str]
    missing_keywords: List[str]
    resume_improvements: List[str]
    recommended_projects: List[str]
    recommended_certifications: List[str]
    summary: str