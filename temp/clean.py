import re
import json

def clean_text(text):
    # Remove page numbers (e.g., "Page xxii" or "Page i")
    text = re.sub(r'Page\s+\w+', '', text, flags=re.IGNORECASE)
    
    # Remove dates (e.g., "8/19/2011" or "08/10/2011")
    text = re.sub(r'\d{1,2}/\d{1,2}/\d{4}', '', text)
    
    # Remove time stamps (e.g., "12:23:07 PM")
    text = re.sub(r'\d{1,2}:\d{2}:\d{2}\s*(AM|PM)', '', text, flags=re.IGNORECASE)
    
    # Remove file names (e.g., "something.indd")
    text = re.sub(r'\b\w+\.indd\b', '', text, flags=re.IGNORECASE)
    
    # Remove publication and copyright lines
    text = re.sub(r'Published by[^\n]+', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Copyright ©[^\n]+', '', text, flags=re.IGNORECASE)
    
    # Remove URLs
    text = re.sub(r'http[s]?://\S+', '', text)
    text = re.sub(r'www\.[^\s]+', '', text, flags=re.IGNORECASE)
    
    # Remove specific legal sections if present
    text = re.sub(r'Limit of Liability/Disclaimer of Warranty:.*?(?=For|$)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'Library of Congress Control Number:.*?(?=Trademarks:|$)', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'Trademarks:.*', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove common publisher names
    text = re.sub(r'John Wiley & Sons,? Inc\.?', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Wiley', '', text, flags=re.IGNORECASE)
    
    # Remove standalone numbers (if not needed)
    text = re.sub(r'\b\d+\b', '', text)
    
    # Remove parts like "com/go/permissions"
    text = re.sub(r'\bcom\/\S+', '', text, flags=re.IGNORECASE)
    
    # --- Additional Cleaning Rules ---
    # Remove a common prefix (e.g., "Stuttard fﬁ V4 - ") at the start of the text.
    text = re.sub(r'^Stuttard\s+[ﬂfﬁ]+\s+V\d+\s*-\s*', '', text, flags=re.IGNORECASE)
    
    # Remove standalone Roman numerals (e.g., "i", "ii", "iii", "xxii") as isolated tokens
    text = re.sub(r'\b[ivxlcdm]+\b', '', text, flags=re.IGNORECASE)
    
    # Remove text from certain legal disclaimers if needed
    text = re.sub(r'No warranty.*', '', text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r'For general information about our other products.*', '', text, flags=re.IGNORECASE | re.DOTALL)
    
    # Clean up extra whitespace and adjust punctuation spacing
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'\s([,.!?;:])', r'\1', text)
    
    return text.strip()

# File paths (make sure "book.jsonl" is in the same folder)
input_file = "book.jsonl"          # Original file with raw text
output_file = "book_cleaned.jsonl"   # File to save cleaned text

def main():
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            data = json.loads(line)
            if "text" in data:
                data["text"] = clean_text(data["text"])
                outfile.write(json.dumps(data, ensure_ascii=False) + "\n")
    print(f"Cleaned file saved as: {output_file}")

if __name__ == "__main__":
    main()
