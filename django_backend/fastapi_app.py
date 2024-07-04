from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel

app = FastAPI()

client = MongoClient('mongodb://localhost:27017')
db = client.sentiment_analysis_db
collection = db.sentiments

class Sentiment(BaseModel):
    text: str
    sentiment: str

@app.post("/sentiment/")
async def create_sentiment(sentiment: Sentiment):
    result = collection.insert_one(sentiment.dict())
    return {"_id": str(result.inserted_id)}

@app.get("/sentiment/{id}")
async def read_sentiment(id: str):
    sentiment = collection.find_one({"_id": ObjectId(id)})
    if sentiment is None:
        raise HTTPException(status_code=404, detail="Sentiment not found")
    return sentiment
