import json
import re
import nltk
from nltk.tokenize import sent_tokenize

# Download necessary resources for sentence tokenization
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
                print("Error reading line:", e)
    return texts

def combine_texts(texts):
    # Combine all texts into a single text (assumes the order is correct)
    return "\n".join(texts)

def additional_cleaning(text):
    # Remove some legal and publishing patterns
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
    # Remove web URLs
    text = re.sub(r'http[s]?://\S+', '', text)
    text = re.sub(r'www\.[^\s]+', '', text, flags=re.IGNORECASE)
    # Remove standalone number sequences (optional)
    text = re.sub(r'\b\d+\b', '', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def segment_text(text, sentences_per_paragraph=5, min_sentences=3):
    # Segment the text into sentences
    sentences = sent_tokenize(text)
    paragraphs = []
    temp = []
    for sentence in sentences:
        if len(sentence.strip()) < 10:
            continue  # Ignore very short sentences
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
    print(f"Formatted data has been saved to: {output_file}")

if __name__ == '__main__':
    input_file = "output_data.jsonl"      # Original extracted file
    output_file = "formatted_data.jsonl"  # Output file after formatting
    
    # Load and combine texts
    texts = load_jsonl(input_file)
    combined_text = combine_texts(texts)
    
    # Perform additional text cleaning
    cleaned_text = additional_cleaning(combined_text)
    
    # Segment the cleaned text into structured paragraphs
    paragraphs = segment_text(cleaned_text, sentences_per_paragraph=5, min_sentences=3)
    
    # Save the paragraphs into a new JSONL file
    save_jsonl(paragraphs, output_file)

