from django.contrib import admin
from .models import Company, Sentiment, SentimentAnalysis, NamedEntity, Keyword, POSTag, AttentionWord

admin.site.register(Company)
admin.site.register(Sentiment)
admin.site.register(SentimentAnalysis)
admin.site.register(NamedEntity)
admin.site.register(Keyword)
admin.site.register(POSTag)
admin.site.register(AttentionWord)