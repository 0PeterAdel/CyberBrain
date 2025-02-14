import json
import re

# قائمة بأنماط النصوص غير التقنية التي نرغب بإزالتها
non_tech_patterns = [
    r'Published by.*?(?=\.)',
    r'Copyright ©.*?(?=\.)',
    r'ISBN:.*?(?=\.)',
    r'Library of Congress Control Number:.*?(?=\.)',
    r'Trademarks:.*?(?=\.)',
    r'Limit of Liability/Disclaimer of Warranty:.*?(?=\.)',
    r'Wiley',
    r'John Wiley & Sons,? Inc\.?'
]

# قائمة بالكلمات المفتاحية الخاصة بالأمن السيبراني
cyber_keywords = [
    "security", "attack", "injection", "penetration", "vulnerability",
    "exploit", "web application", "authentication", "authorization",
    "cyber", "network", "malware"
]

def further_clean(text):
    # إزالة الأنماط غير التقنية
    for pattern in non_tech_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    # تنظيم الفراغات الزائدة
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def is_technical(text):
    # التحقق من احتواء النص على إحدى الكلمات المفتاحية التقنية
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in cyber_keywords)

input_file = "cybersec_training.jsonl"      # ملف بيانات التدريب الحالي
output_file = "cybersec_training_refined.jsonl"  # الملف الناتج بعد التنقية

refined_records = []
with open(input_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        try:
            record = json.loads(line)
            instruction = record.get("instruction", "").strip()
            output_text = record.get("output", "").strip()
            # إجراء التنظيف الإضافي
            cleaned_output = further_clean(output_text)
            # الاحتفاظ بالسجلات التي تحتوي على معلومات تقنية ويكون حجمها أكبر من 20 كلمة
            if is_technical(cleaned_output) and len(cleaned_output.split()) > 20:
                refined_records.append({
                    "instruction": instruction,
                    "output": cleaned_output
                })
        except Exception as e:
            print("Error processing line:", e)

with open(output_file, 'w', encoding='utf-8') as outfile:
    for rec in refined_records:
        outfile.write(json.dumps(rec, ensure_ascii=False) + "\n")

print(f"تم حفظ البيانات المنقحة في الملف: {output_file}")
