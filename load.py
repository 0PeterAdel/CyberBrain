# load.py
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

def get_model():
    model_name = "unsloth/DeepSeek-R1-Distill-Llama-8B"
    max_seq_length = 2048
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")
    
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none"
    )
    model = get_peft_model(model, lora_config)
    print("تم تحميل وتطبيق LoRA على النموذج بنجاح!")
    return model, tokenizer
