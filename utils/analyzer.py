from google.genai import types

from utils.gemini_client import client
from utils.pdf_reader import extract_text_from_pdf
from utils.prompts import SYSTEM_PROMPT, build_prompt
from utils.schema import ResumeAnalysis


def analyze_resume(pdf_path, job_role):

    # Extract text from the uploaded PDF
    resume_text = extract_text_from_pdf(pdf_path)

    # Build the dynamic prompt
    prompt = build_prompt(resume_text, job_role)

    # Send request to Gemini
    response = client.models.generate_content(
        model="gemini-3.6-flash",

        contents=prompt,

        config=types.GenerateContentConfig(

            system_instruction=SYSTEM_PROMPT,

            temperature=0.2,

            max_output_tokens=4096,

            response_mime_type="application/json",

            response_schema=ResumeAnalysis

        )
    )

    print("\n========== RAW RESPONSE ==========")
    print(response)

    print("\n========== PARSED RESPONSE ==========")
    print(response.parsed)

    return response.parsed