import json
import re

# List of non-technical text patterns we want to remove
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

# List of cybersecurity-related keywords
cyber_keywords = [
    "security", "attack", "injection", "penetration", "vulnerability",
    "exploit", "web application", "authentication", "authorization",
    "cyber", "network", "malware"
]

def further_clean(text):
    # Remove non-technical patterns
    for pattern in non_tech_patterns:
        text = re.sub(pattern, '', text, flags=re.IGNORECASE)
    # Normalize excess spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def is_technical(text):
    # Check if the text contains any of the technical keywords
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in cyber_keywords)

input_file = "cybersec_training.jsonl"      # Current training data file
output_file = "cybersec_training_refined.jsonl"  # Output file after refinement

refined_records = []
with open(input_file, 'r', encoding='utf-8') as infile:
    for line in infile:
        try:
            record = json.loads(line)
            instruction = record.get("instruction", "").strip()
            output_text = record.get("output", "").strip()
  

