from unsloth import FastLanguageModel

model_name = "unsloth/DeepSeek-R1-Distill-Llama-8B-unsloth-bnb-4bit"
max_seq_length = 2048

# تحديد خريطة توزيع الأجهزة بحيث تُحمّل بعض المكونات على GPU والبعض الآخر على CPU لتقليل استهلاك الذاكرة.
device_map = {
    "model.embed_tokens": 0,  # تحميل طبقة التضمين على GPU
    "lm_head": 0,             # تحميل الرأس على GPU
    "model.layers": "cpu",    # نقل طبقات النموذج الأساسية إلى CPU
}

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=model_name,
    max_seq_length=max_seq_length,
    load_in_4bit=True,
    device_map=device_map,
)

print("تم تحميل النموذج بنجاح مع توزيع الأجهزة المخصص!")
