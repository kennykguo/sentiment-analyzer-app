from fastapi import FastAPI
from pydantic import BaseModel
from .sentiment_model import sentiment_model

app = FastAPI()

class SentimentRequest(BaseModel):
    text: str

@app.post("/analyze_sentiment")
async def analyze_sentiment(request: SentimentRequest):
    # Analyze sentiment using the loaded model
    sentiment_score = sentiment_model.analyze_sentiment(request.text)
    return {"sentiment_score": sentiment_score}