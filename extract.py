import PyPDF2

try:
    with open("Amruta_Resume.pdf", "rb") as file:
        reader = PyPDF2.PdfReader(file)
        with open("resume_text.txt", "w", encoding="utf-8") as out:
            for page in reader.pages:
                out.write(page.extract_text() + "\n")
        print("Done")
except Exception as e:
    print(f"Error reading PDF: {e}")
