# trainer.py
from load import get_model  # Or from LoRA if there is a similar function
from datasets import load_dataset
from transformers import TrainingArguments, Trainer

# Load the model and tokenizer
model, tokenizer = get_model()

# Load the dataset (assume it's available or modify the path as needed)
dataset = load_dataset("json", data_files={"train": "Create-DataSet/out/1.jsonl", "test": "Create-DataSet/out/1.jsonl"})

# Define a prompt template for the task
prompt_template = """Below is an instruction that describes a cybersecurity task. Write a detailed response that appropriately completes the request.

### Instruction:
{instruction}
### Response:
"""

def preprocess_function(examples):
    # Format each instruction with the prompt template
    inputs = [prompt_template.format(instruction=inst) for inst in examples["instruction"]]
    # Tokenize the inputs and truncate to fit the model's maximum input length
    model_inputs = tokenizer(inputs, max_length=2048, truncation=True)
    return model_inputs

# Apply preprocessing to the dataset (batched for efficiency)
tokenized_dataset = dataset.map(preprocess_function, batched=True)

# Set up the training parameters
training_args = TrainingArguments(
    output_dir="./finetuned_deepseek_ethics_cpu",  # Directory to save the fine-tuned model
    num_train_epochs=3,                          # Number of training epochs
    per_device_train_batch_size=1,               # Batch size per device (small size to fit CPU)
    gradient_accumulation_steps=8,               # Gradient accumulation steps to simulate larger batch size
    evaluation_strategy="no",                    # No evaluation during training
    save_strategy="epoch",                       # Save model at the end of each epoch
    learning_rate=5e-5,                          # Learning rate for training
    logging_steps=10,                            # Log every 10 steps
    report_to="none"                             # Disable external reporting (e.g., to TensorBoard)
)

# Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],    # Use the training dataset
    eval_dataset=tokenized_dataset["test"],      # Use the test dataset
    tokenizer=tokenizer,                         # Use the tokenizer
)

# Start training the model
trainer.train()
