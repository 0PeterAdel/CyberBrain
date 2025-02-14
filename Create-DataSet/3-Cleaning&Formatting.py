import json

# List of keywords related to cybersecurity (can be modified and expanded as needed)
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
                # If the text contains technical information related to cybersecurity
                if is_cybersecurity_text(text) and len(text) > 50:
                    # Here you can adjust the instruction template as needed
                    instruction = "Explain the following concept or technique in cybersecurity:"
                    training_pair = {
                        "instruction": instruction,
                        "input": "",
                        "output": text
                    }
                    training_data.append(training_pair)
            except Exception as e:
                print("Error processing the line:", e)
    # Save the pairs in a JSONL file
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for pair in training_data:
            outfile.write(json.dumps(pair, ensure_ascii=False) + "\n")
    print(f"Training data has been saved in the file: {output_file}")

# Modify the file names according to the sequence of previous formatting steps
input_file = "formatted_data.jsonl"  # The formatted file containing the paragraphs
output_file = "cybersecurity_training_data.jsonl"
create_training_pairs(input_file, output_file)

