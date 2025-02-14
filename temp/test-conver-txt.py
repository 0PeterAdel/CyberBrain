import PyPDF2
import json

# اسم ملف PDF
pdf_file = "The Web Application Hackers Handbook 2nd Edition.pdf"

# فتح ملف الـ PDF
with open(pdf_file, "rb") as f:
    reader = PyPDF2.PdfReader(f)
    data = []
    
    # استخراج النص من كل صفحة
    for page in reader.pages:
        text = page.extract_text()
        if text:
            # يمكنك تقسيم النص إلى فقرات باستخدام فاصل مثل "\n\n"
            paragraphs = text.split("\n\n")
            for para in paragraphs:
                para = para.strip()
                if para:
                    data.append({"text": para})

# حفظ البيانات في ملف JSONL
output_file = "book.jsonl"
with open(output_file, "w", encoding="utf-8") as out_f:
    for item in data:
        out_f.write(json.dumps(item, ensure_ascii=False) + "\n")

print(f"تم حفظ البيانات في الملف: {output_file}")
