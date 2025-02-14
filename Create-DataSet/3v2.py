import json
import re

# Regular expression to detect chapter titles; tries to match text starting with "C H A P T E R" or "Chapter"
chapter_header_pattern = re.compile(r'^(?:C\s*H\s*A\s*P\s*T\s*E\s*R|Chapter)\s*(.*)', re.IGNORECASE)

input_file = "formatted_data.jsonl"       # The current file containing formatted paragraphs
output_file = "cybersec_training.jsonl"    # The new file that will contain the training examples

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
        # Check if the text is a chapter title
        header_match = chapter_header_pattern.match(text)
        if header_match:
            # If there was a previous chapter, store its content
            if current_chapter_title and current_content:
                chapters.append({
                    "instruction": current_chapter_title,
                    "output": " ".join(current_content).strip()
                })
            # Update the current chapter title to the new title (which may be the text following the word "Chapter")
            current_chapter_title = header_match.group(1).strip()
            current_content = []  # Reinitialize the content for the new chapter
        else:
            # If it's not a chapter title and we are in an existing chapter, add the text to the content
            if current_chapter_title:
                current_content.append(text)
            else:
                # If no chapter title has appeared yet, we can either ignore these paragraphs or treat them as an introduction
                pass

# Add the last chapter if exists
if current_chapter_title and current_content:
    chapters.append({
        "instruction": current_chapter_title,
        "output": " ".join(current_content).strip()
    })

# Save the examples to a new JSONL file
with open(output_file, 'w', encoding='utf-8') as f:
    for chapter in chapters:
        f.write(json.dumps(chapter, ensure_ascii=False) + "\n")

print(f"Training data for {len(chapters)} chapters has been created in the file: {output_file}")

