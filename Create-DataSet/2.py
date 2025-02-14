import json
import re
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def load_jsonl(file_path):
    texts = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if "text" in data:
                    texts.append(data["text"])
            except Exception as e:
                print("خطأ في قراءة السطر:", e)
    return texts

def combine_texts(texts):
    # دمج جميع النصوص في نص واحد (يفترض أن الترتيب مناسب)
    return "\n".join(texts)

def additional_cleaning(text):
    # إزالة بعض الأنماط القانونية والناشرة
    patterns = [
        r'Published by.*?(?=\.)',
        r'Copyright ©.*?(?=\.)',
        r'ISBN:.*?(?=\.)',
        r'Library of Congress Control Number:.*?(?=\.)',
        r'Trademarks:.*?(?=\.)',
        r'Limit of Liability/Disclaimer of Warranty:.*?(?=\.)'
    ]
    for pat in patterns:
        text = re.sub(pat, '', text, flags=re.IGNORECASE)
    # إزالة روابط الإنترنت
    text = re.sub(r'http[s]?://\S+', '', text)
    text = re.sub(r'www\.[^\s]+', '', text, flags=re.IGNORECASE)
    # إزالة تسلسلات أرقام منفردة (اختياري)
    text = re.sub(r'\b\d+\b', '', text)
    # إزالة فراغات زائدة
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def segment_text(text, sentences_per_paragraph=5, min_sentences=3):
    # تقسيم النص إلى جمل
    sentences = sent_tokenize(text)
    paragraphs = []
    temp = []
    for sentence in sentences:
        if len(sentence.strip()) < 10:
            continue  # تجاهل الجمل القصيرة جدًا
        temp.append(sentence.strip())
        if len(temp) >= sentences_per_paragraph:
            paragraph = " ".join(temp)
            if len(sent_tokenize(paragraph)) >= min_sentences:
                paragraphs.append(paragraph)
            temp = []
    if temp and len(sent_tokenize(" ".join(temp))) >= min_sentences:
        paragraphs.append(" ".join(temp))
    return paragraphs

def save_jsonl(paragraphs, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for para in paragraphs:
            record = {"text": para}
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"تم حفظ البيانات المنسقة في الملف: {output_file}")

if __name__ == '__main__':
    input_file = "output_data.jsonl"      # الملف الأصلي المستخرج
    output_file = "formatted_data.jsonl"  # الملف الناتج بعد التنسيق
    
    # تحميل ودمج النصوص
    texts = load_jsonl(input_file)
    combined_text = combine_texts(texts)
    
    # تنظيف إضافي للنص
    cleaned_text = additional_cleaning(combined_text)
    
    # تقسيم النص إلى فقرات منظمة
    paragraphs = segment_text(cleaned_text, sentences_per_paragraph=5, min_sentences=3)
    
    # حفظ الفقرات في ملف JSONL جديد
    save_jsonl(paragraphs, output_file)
