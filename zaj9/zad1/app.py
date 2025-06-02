from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

class TextIn(BaseModel):
    text: str

@app.post("/summarize")
def summarize_text(data: TextIn):
    summary = summarizer(data.text, max_length=130, min_length=30, do_sample=False)
    return {"summary": summary[0]["summary_text"]}
