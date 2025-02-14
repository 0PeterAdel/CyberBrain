import json

data = []
# قراءة الكتاب من ملف نصي
with open("book.txt", "r", encoding="utf-8") as f:
    # يمكن تقسيم الكتاب إلى فقرات باستخدام فاصل مثل سطر فارغ
    paragraphs = f.read().split("\n\n")
    for para in paragraphs:
        cleaned_para = para.strip()
        if cleaned_para:
            data.append({"text": cleaned_para})

# حفظ البيانات في ملف JSONL
with open("book.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
