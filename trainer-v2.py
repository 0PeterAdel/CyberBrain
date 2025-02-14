from load import get_model  # Ensure the load.py file contains the get_model() function that returns (model, tokenizer)
from datasets import load_dataset
from transformers import TrainingArguments, Trainer

# Load the model and tokenizer
model, tokenizer = get_model()

# Load the training dataset (make sure to adjust the file path if necessary)
dataset = load_dataset("json", data_files={"train": "../path/to/cybersecurity_training_data.jsonl",
                                             "test": "../path/to/cybersecurity_training_data.jsonl"})

# Template for formatting the data into a conversation-like format
prompt_template = """Below is an instruction that describes a cybersecurity task. Write a detailed response that appropriately completes the request.

### Instruction:
{instruction}
### Response:
"""

def preprocess_function(examples):
    # Format the input instructions according to the prompt template
    inputs = [prompt_template.format(instruction=inst) for inst in examples["instruction"]]
    model_inputs = tokenizer(inputs, max_length=2048, truncation=True)
    # Add labels that are the same as input_ids to compute the loss
    model_inputs["labels"] = model_inputs["input_ids"].copy()
    return model_inputs

# Apply the preprocessing function to the dataset
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Set up the training arguments
training_args = TrainingArguments(
    output_dir="./finetuned_deepseek_ethics_cpu",  # Output directory for the model
    num_train_epochs=3,                          # Number of training epochs
    per_device_train_batch_size=1,               # Small batch size to fit CPU
    gradient_accumulation_steps=8,               # Accumulate small batches for a larger effective batch size
    evaluation_strategy="no",                    # Disable evaluation during training
    save_strategy="epoch",                       # Save the model after every epoch
    learning_rate=5e-5,                          # Learning rate
    logging_steps=10,                            # Log every 10 steps
    report_to="none"                             # Disable reporting to external services
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],    # Use the training dataset
    eval_dataset=tokenized_dataset["test"],      # Use the test dataset
    tokenizer=tokenizer,
)

# Start training
trainer.train()
