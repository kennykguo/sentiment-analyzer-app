# Open Django shell
python manage.py shell

# In the shell:
from api.models import Company, Sentiment

# Get the company with ID {id}
company = Company.objects.get(id=73)

# Retrieve and print sentiments
sentiments = Sentiment.objects.filter(company=company)
for sentiment in sentiments:
    print(f"Review: {sentiment.review}, Sentiment Score: {sentiment.sentiment_score}")
