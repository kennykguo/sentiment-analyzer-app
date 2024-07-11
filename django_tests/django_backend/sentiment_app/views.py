from django.shortcuts import render, redirect
from .models import Sentiment
from django.utils import timezone
import httpx

async def index(request):
    if request.method == 'POST':
        text = request.POST.get('sentiment')
        sentiment = Sentiment.create(text)
        
        # Call FastAPI endpoint
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8000/analyze_sentiment", json={"text": text})
            sentiment_data = response.json()
        
        sentiment.score = sentiment_data['sentiment_score']
        sentiment.created_at = timezone.now()
        sentiment.save()
        return redirect('result', sentiment_id=sentiment._id)
    
    sentiments = Sentiment.get_all()
    return render(request, 'sentiment_app/index.html', {'sentiments': sentiments})

def result(request, sentiment_id):
    sentiment = Sentiment.get(sentiment_id)
    return render(request, 'sentiment_app/result.html', {'sentiment': sentiment})

def delete(request, sentiment_id):
    sentiment = Sentiment.get(sentiment_id)
    if sentiment:
        sentiment.delete()
    return redirect('index')