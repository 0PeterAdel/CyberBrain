from load import get_model
from peft import LoraConfig, get_peft_model

model, tokenizer = get_model()

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none"
)
model = get_peft_model(model, lora_config)

print("Model is available in LoRA.py")
