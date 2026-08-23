from flask import Flask, render_template, request
import os

from utils.analyzer import analyze_resume

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# ----------------------------
# Home Page
# ----------------------------
@app.route("/")
# If the browser requests the URL /, run the function connected to it.
def home():
    return render_template("index.html")


# ----------------------------
# Analyze Resume
# ----------------------------
@app.route("/analyze", methods=["POST"])
def analyze():

    # Check if a file was uploaded
    if "resume" not in request.files:
        return "No file uploaded."

    uploaded_file = request.files["resume"]

    # Check if filename is empty
    if uploaded_file.filename == "":
        return "Please select a PDF."

    # Allow only PDF files
    if not uploaded_file.filename.lower().endswith(".pdf"):
        return "Only PDF files are allowed."

    # Get job role
    job_role = request.form.get("job_role", "").strip()

    if job_role == "":
        return "Please enter a target job role."

    # Save uploaded PDF
    pdf_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        uploaded_file.filename
    )

    uploaded_file.save(pdf_path)

    try:
        # Analyze Resume
        result = analyze_resume(
            pdf_path,
            job_role
        )

    finally:
        # Delete uploaded file
        if os.path.exists(pdf_path):
            os.remove(pdf_path)

    # File name without extension
    filename = os.path.splitext(uploaded_file.filename)[0]

    # Show Results
    return render_template(
        "result.html",
        result=result,
        filename=filename,
        job_role=job_role
    )


# ----------------------------
# Run Flask
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)