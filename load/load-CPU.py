from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "unsloth/DeepSeek-R1-Distill-Llama-8B" 
max_seq_length = 2048

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="cpu")
