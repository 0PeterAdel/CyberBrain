import json

data = []
# Reading the book from a text file
with open("book.txt", "r", encoding="utf-8") as f:
    # You can split the book into paragraphs using a separator like a blank line
    paragraphs = f.read().split("\n\n")
    for para in paragraphs:
        cleaned_para = para.strip()
        if cleaned_para:
            data.append({"text": cleaned_para})

# Save the data to a JSONL file
with open("book.jsonl", "w", encoding="utf-8") as f:
    for item in data:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")

