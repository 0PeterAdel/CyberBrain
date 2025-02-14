import json
import re

# النمط الأصلي للبحث عن "CHAPTER" أو "Chapter"
pattern_chapter = re.compile(r'^(?:C\s*H\s*A\s*P\s*T\s*E\s*R|Chapter)\s*(.*)', re.IGNORECASE)

def is_header(text):
    """
    تتحقق من كون النص عنوان فصل.
    تعود (True, header_title) إذا كان عنوان الفصل، و(False, None) خلاف ذلك.
    """
    # التحقق من النمط الأصلي
    match = pattern_chapter.match(text)
    if match:
        return True, match.group(1).strip()
    # التحقق إذا كان النص بأحرف كبيرة وعدد كلماته قليل (مثلاً ≤ 10)
    words = text.split()
    if words and len(words) <= 10 and text == text.upper():
        return True, text.strip()
    return False, None

input_file = "formatted_data.jsonl"       # الملف الحالي الذي يحتوي على الفقرات المنسقة
output_file = "cybersec_training.jsonl"     # الملف الجديد الذي سيحتوي على أمثلة التدريب

chapters = []
current_chapter_title = None
current_content = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
        except Exception as e:
            print("خطأ في قراءة السطر:", e)
            continue
        text = data.get("text", "").strip()
        header_detected, header_title = is_header(text)
        if header_detected:
            # إذا كان هناك فصل سابق، احفظه
            if current_chapter_title and current_content:
                chapters.append({
                    "instruction": current_chapter_title,
                    "output": " ".join(current_content).strip()
                })
            current_chapter_title = header_title
            current_content = []
        else:
            # إذا تم العثور على عنوان فصل بالفعل، نضيف النص للمحتوى
            if current_chapter_title:
                current_content.append(text)
            else:
                # إذا لم يتم العثور على عنوان فصل بعد، يمكن اعتبارها مقدمة
                current_content.append(text)

# إضافة الفصل الأخير إذا وجد
if current_chapter_title and current_content:
    chapters.append({
        "instruction": current_chapter_title,
        "output": " ".join(current_content).strip()
    })
# إذا لم يتم التعرف على أي عنوان فصل، نعتبر النص بأكمله مقدمة
elif not current_chapter_title and current_content:
    chapters.append({
        "instruction": "Introduction",
        "output": " ".join(current_content).strip()
    })

with open(output_file, 'w', encoding='utf-8') as f:
    for chapter in chapters:
        f.write(json.dumps(chapter, ensure_ascii=False) + "\n")

print(f"تم إنشاء بيانات التدريب لـ {len(chapters)} فصول في الملف: {output_file}")
