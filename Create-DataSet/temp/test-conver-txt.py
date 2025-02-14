import PyPDF2
import json

# Name of the PDF file
pdf_file = "The Web Application Hackers Handbook 2nd Edition.pdf"

# Open the PDF file
with open(pdf_file, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    data = []
    
    # Extract text from each page
    for page in reader.pages:
        text = page.extract_text()
        if text:
            # You can split the text into paragraphs using a separator like "\n\n"
            paragraphs = text.split("\n\n")
            for para in paragraphs:
                para = para.strip()
                if para:
                    data.append({"text": para})

# Save the data to a JSONL file
output_file = "book.jsonl"
with open(output_file, "w", encoding="utf-8") as out_f:
    for item in data:
        out_f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"Data has been saved to the file: {output_file}")

