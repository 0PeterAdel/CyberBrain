# trainer.py
from load import get_model  # أو من LoRA إذا كان هناك دالة مشابهة
from datasets import load_dataset
from transformers import TrainingArguments, Trainer

# الحصول على النموذج والمُحول
model, tokenizer = get_model()

# تحميل مجموعة البيانات (افترض أنها موجودة أو قم بتعديل المسار حسب الحاجة)
dataset = load_dataset("json", data_files={"train": "Create-DataSet/out/1.jsonl", "test": "Create-DataSet/out/1.jsonl"})

prompt_template = """Below is an instruction that describes a cybersecurity task. Write a detailed response that appropriately completes the request.

### Instruction:
{instruction}
### Response:
"""

def preprocess_function(examples):
    inputs = [prompt_template.format(instruction=inst) for inst in examples["instruction"]]
    model_inputs = tokenizer(inputs, max_length=2048, truncation=True)
    return model_inputs

tokenized_dataset = dataset.map(preprocess_function, batched=True)

training_args = TrainingArguments(
    output_dir="./finetuned_deepseek_ethics_cpu",
    num_train_epochs=3,
    per_device_train_batch_size=1,
    gradient_accumulation_steps=8,
    evaluation_strategy="no",
    save_strategy="epoch",
    learning_rate=5e-5,
    logging_steps=10,
    report_to="none"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"],
    eval_dataset=tokenized_dataset["test"],
    tokenizer=tokenizer,
)

trainer.train()
