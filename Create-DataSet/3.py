import json

# قائمة الكلمات المفتاحية ذات الصلة بالأمن السيبراني (يمكن تعديلها وتوسيعها حسب الحاجة)
keywords = ["attack", "hacking", "injection", "vulnerability", "security", "penetration", "exploit", "session", "authentication", "sql", "xss", "csrf"]

def is_cybersecurity_text(text):
    lower_text = text.lower()
    return any(keyword in lower_text for keyword in keywords)

def create_training_pairs(input_file, output_file):
    training_data = []
    with open(input_file, 'r', encoding='utf-8') as infile:
        for line in infile:
            try:
                data = json.loads(line)
                text = data.get("text", "").strip()
                # إذا كان النص يحتوي على معلومات تقنية متعلقة بالأمن السيبراني
                if is_cybersecurity_text(text) and len(text) > 50:
                    # هنا يمكن تعديل نموذج التعليمات حسب ما تحتاج
                    instruction = "اشرح المفهوم أو التقنية التالية في مجال الأمن السيبراني:"
                    training_pair = {
                        "instruction": instruction,
                        "input": "",
                        "output": text
                    }
                    training_data.append(training_pair)
            except Exception as e:
                print("خطأ في معالجة السطر:", e)
    # حفظ الأزواج في ملف JSONL
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for pair in training_data:
            outfile.write(json.dumps(pair, ensure_ascii=False) + "\n")
    print(f"تم حفظ بيانات التدريب في الملف: {output_file}")

# قم بتعديل أسماء الملفات حسب ترتيب خطوات التنسيق السابقة
input_file = "formatted_data.jsonl"  # الملف المنسق الذي يحتوي على الفقرات
output_file = "cybersecurity_training_data.jsonl"
create_training_pairs(input_file, output_file)
