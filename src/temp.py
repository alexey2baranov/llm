import torch
from transformers import (
    AutoModel,
    AutoModelForCausalLM,
    AutoModelForSeq2SeqLM,
    AutoModelForSequenceClassification,
    AutoTokenizer,
    pipeline,
    set_seed,
)

# checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# model = AutoModelForSequenceClassification.from_pretrained(checkpoint)
# sequences = [
#     "I've been waiting for a HuggingFace course my whole life.", "So have I!"]

# tokens = tokenizer(sequences, padding=True,
#                    truncation=True, return_tensors="pt")
# output = model(**tokens)

# print(tokenizer.decode(output[0], skip_special_tokens=True))


tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2", device_map="auto", load_in_8bit=False)

input_ids = tokenizer("Hello, I'm a language model,", return_tensors="pt")
output = model.generate(**input_ids, max_length=30, do_sample=True, temperature=0.7)

print(tokenizer.decode(output[0], skip_special_tokens=True))


# generator = pipeline('text-generation', model='gpt2')
# set_seed(42)
# output = generator("Hello, I'm a language model,",
#                    max_length=30, num_return_sequences=5)
# print(output)
