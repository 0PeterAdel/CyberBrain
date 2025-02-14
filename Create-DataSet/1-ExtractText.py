import re
import json
import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')  # Download NLTK tokenizer data


def extract_text_from_pdf(pdf_path):
    """Extracts raw text from a PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text


def clean_text(raw_text):
    """Cleans extracted text by removing unwanted characters and formatting."""
    # Remove form feed characters and extra spaces
    text = raw_text.replace("\f", " ")
    text = re.sub(r'\s+', ' ', text)  # Normalize whitespace

    # Remove headers, footers, and page numbers
    text = re.sub(r'Page\s+\d+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\b\d{1,2}/\d{1,2}/\d{4}\b', '', text)  # Dates
    text = re.sub(r'\b\d{1,2}:\d{2}:\d{2}\s*(AM|PM)?\b', '', text, flags=re.IGNORECASE)  # Time stamps
    
    # Remove standalone numbers (likely to be page numbers or figure references)
    text = re.sub(r'\b\d+\b', '', text)
    
    return text.strip()


def split_into_paragraphs(cleaned_text, sentences_per_paragraph=5):
    """Splits text into structured paragraphs for AI training."""
    sentences = sent_tokenize(cleaned_text)
    paragraphs = []
    temp_paragraph = []

    for i, sent in enumerate(sentences):
        temp_paragraph.append(sent)
        if (i + 1) % sentences_per_paragraph == 0:
            paragraphs.append(" ".join(temp_paragraph))
            temp_paragraph = []
    
    if temp_paragraph:
        paragraphs.append(" ".join(temp_paragraph))

    return paragraphs


def save_to_jsonl(paragraphs, output_file):
    """Saves extracted paragraphs to a JSONL file."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for para in paragraphs:
            data = {"text": para}
            outfile.write(json.dumps(data, ensure_ascii=False) + "\n")
    print(f"Processed data saved to: {output_file}")


def process_pdf_to_jsonl(pdf_path, output_file):
    """Extracts, cleans, and saves text from PDF to JSONL."""
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)
    paragraphs = split_into_paragraphs(cleaned_text)
    save_to_jsonl(paragraphs, output_file)


# Example usage
pdf_path = "book.pdf"  # Replace with actual PDF file path
output_file = "output_data.jsonl"
process_pdf_to_jsonl(pdf_path, output_file)
