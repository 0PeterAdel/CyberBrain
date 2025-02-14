import json
import re

# تعبير نمطي لاكتشاف عناوين الفصول؛ يحاول التعرف على نص يبدأ بـ "C H A P T E R" أو "Chapter"
chapter_header_pattern = re.compile(r'^(?:C\s*H\s*A\s*P\s*T\s*E\s*R|Chapter)\s*(.*)', re.IGNORECASE)

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
        # التحقق مما إذا كان النص هو عنوان فصل
        header_match = chapter_header_pattern.match(text)
        if header_match:
            # إذا كان هناك فصل سابق تم تجميع محتواه، نقوم بتخزينه
            if current_chapter_title and current_content:
                chapters.append({
                    "instruction": current_chapter_title,
                    "output": " ".join(current_content).strip()
                })
            # تحديث عنوان الفصل الحالي إلى العنوان الجديد (قد يكون العنوان عبارة عن النص الذي يلي الكلمة Chapter)
            current_chapter_title = header_match.group(1).strip()
            current_content = []  # إعادة تهيئة المحتوى للفصل الجديد
        else:
            # إذا لم يكن النص عنوان فصل ونفترض أننا ضمن فصل محدد، نضيف النص للمحتوى
            if current_chapter_title:
                current_content.append(text)
            else:
                # إذا لم يظهر عنوان فصل بعد، يمكن تجاهل هذه الفقرات أو استخدامها كمقدمة
                pass

# إضافة آخر فصل إذا وجد
if current_chapter_title and current_content:
    chapters.append({
        "instruction": current_chapter_title,
        "output": " ".join(current_content).strip()
    })

# حفظ الأمثلة إلى ملف JSONL جديد
with open(output_file, 'w', encoding='utf-8') as f:
    for chapter in chapters:
        f.write(json.dumps(chapter, ensure_ascii=False) + "\n")

print(f"تم إنشاء بيانات التدريب لـ {len(chapters)} فصول في الملف: {output_file}")
