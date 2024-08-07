import os
import django
import pandas as pd
from django.db import transaction

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from api.models import Company, Sentiment

def import_sentiments_from_excel():
    sentiment_folder = os.path.join(os.path.dirname(__file__), 'sentiment_data')
    
    for filename in os.listdir(sentiment_folder):
        if filename.endswith('.xlsx'):
            try:
                company_id = int(filename.split('.')[0])
                company = Company.objects.get(id=company_id)
            except (ValueError, Company.DoesNotExist):
                print(f"Invalid company ID or company not found. Skipping file: {filename}")
                continue
            
            file_path = os.path.join(sentiment_folder, filename)
            df = pd.read_excel(file_path, header=None, names=['review'])
            
            with transaction.atomic():
                for _, row in df.iterrows():
                    Sentiment.objects.create(
                        company=company,
                        review=row['review'],
                        sentiment_score=0.0  # Default value for sentiment_score
                    )
            
            print(f"Processed sentiments for company ID: {company_id}")

import_sentiments_from_excel()