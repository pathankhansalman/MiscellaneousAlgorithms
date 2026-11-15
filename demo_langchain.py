from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from langchain_core.runnables import RunnableLambda, RunnablePassthrough

MODEL_ID = "Qwen/Qwen2.5-0.5B"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID, torch_dtype=torch.float32)

def generate_next_word(prompt: str) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        output = model.generate(**inputs, max_new_tokens=1, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(output[0, inputs.input_ids.shape[-1]:], skip_special_tokens=True).strip()

def get_word_length(data: dict) -> int:
    return len(data["next_word"])

# LangChain LCEL linear pipeline using the pipe operator `|`
chain = (
    {"prompt": RunnablePassthrough()}
    | RunnablePassthrough.assign(next_word=RunnableLambda(lambda x: generate_next_word(x["prompt"])))
    | RunnablePassthrough.assign(word_len=RunnableLambda(get_word_length))
)

sentence = "The capital of France is"
res = chain.invoke(sentence)

print(f"Prompt: '{res['prompt']}'")
print(f"Next Word: '{res['next_word']}'")
print(f"Word Length (from tool): {res['word_len']}")
