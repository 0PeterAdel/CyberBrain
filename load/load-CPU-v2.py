from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

model_name = "unsloth/DeepSeek-R1-Distill-Llama-8B"  # تأكد من اختيار النموذج المناسب
max_seq_length = 2048

# تحميل النموذج والمحول على الـ CPU
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none"
)

# الآن يتم تطبيق LoRA على النموذج
model = get_peft_model(model, lora_config)
