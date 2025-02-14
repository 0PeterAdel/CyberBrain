import json
import re

# The original pattern to search for "CHAPTER" or "Chapter"
pattern_chapter = re.compile(r'^(?:C\s*H\s*A\s*P\s*T\s*E\s*R|Chapter)\s*(.*)', re.IGNORECASE)

def is_header(text):
    """
    Checks if the text is a chapter header.
    Returns (True, header_title) if it's a chapter title, and (False, None) otherwise.
    """
    # Check for the original pattern
    match = pattern_chapter.match(text)
    if match:
        return True, match.group(1).strip()
    # Check if the text is in uppercase and contains few words (e.g., ≤ 10)
    words = text.split()
    if words and len(words) <= 10 and text == text.upper():
        return True, text.strip()
    return False, None

input_file = "formatted_data.jsonl"       # The current file that contains the formatted paragraphs
output_file = "cybersec_training.jsonl"     # The new file that will contain the training examples

chapters = []
current_chapter_title = None
current_content = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
        except Exception as e:
            print("Error reading line:", e)
            continue
        text = data.get("text", "").strip()
        header_detected, header_title = is_header(text)
        if header_detected:
            # If there was a previous chapter, save it
            if current_chapter_title and current_content:
                chapters.append({
                    "instruction": current_chapter_title,
                    "output": " ".join(current_content).strip()
                })
            current_chapter_title = header_title
            current_content = []
        else:
            # If a chapter title has already been found, add the text to the content
            if current_chapter_title:
                current_content.append(text)
            else:
                # If no chapter title has been found yet, consider it an introduction
                current_content.append(text)

# Add the last chapter if found
if current_chapter_title and current_content:
    chapters.append({
        "instruction": current_chapter_title,
        "output": " ".join(current_content).strip()
    })
# If no chapter title was found, consider the entire text as an introduction
elif not current_chapter_title and current_content:
    chapters.append({
        "instruction": "Introduction",
        "output": " ".join(current_content).strip()
    })

with open(output_file, 'w', encoding='utf-8') as f:
    for chapter in chapters:
        f.write(json.dumps(chapter, ensure_ascii=False) + "\n")

print(f"Training data for {len(chapters)} chapters created in the file: {output_file}")

