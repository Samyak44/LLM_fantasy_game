from fastapi import FastAPI, Query
from pydantic import BaseModel
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel

app = FastAPI(title="Fantasy Name Generator API")

# Load model and tokenizer
MODEL_PATH = "fantasy-gpt2-model"
tokenizer = GPT2Tokenizer.from_pretrained(MODEL_PATH)
model = GPT2LMHeadModel.from_pretrained(MODEL_PATH)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

@app.get("/status")
def status():
    return {
        "status": "ok",
        "model": "fine-tuned GPT-2",
        "task": "fantasy name generation"
    }

@app.get("/generate")
def generate(prompt: str = Query(...), max_length: int = 15, num_return_sequences: int = 1):
    results = generator(prompt, max_length=max_length, num_return_sequences=num_return_sequences)
    return {"results": [r["generated_text"] for r in results]}