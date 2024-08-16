from django.core.management.base import BaseCommand
from api.models import Company, SentimentAnalysis

class Command(BaseCommand):
    help = 'Display sentiments and statistics for a specific company ID'

    def add_arguments(self, parser):
        parser.add_argument('company_id', type=int, help='ID of the company to display statistics for')

    def handle(self, *args, **options):
        company_id = options['company_id']
        try:
            company = Company.objects.get(id=company_id)
        except Company.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Company with ID {company_id} does not exist.'))
            return

        self.stdout.write(self.style.SUCCESS(f'Company: {company.name} (ID: {company.id})'))
        self.stdout.write(self.style.SUCCESS('-' * 50))

        sentiments = SentimentAnalysis.objects.filter(company=company)
        if not sentiments.exists():
            self.stdout.write(self.style.NOTICE(f'No sentiments found for Company ID {company_id}.'))
            return

        for sentiment in sentiments:
            self.stdout.write(self.style.SUCCESS(f'ID: {sentiment.id}'))
            self.stdout.write(f'Review: {sentiment.review}')
            self.stdout.write(f'VADER Score: {sentiment.vader_score}')
            self.stdout.write(f'Prediction: {sentiment.model_prediction}')
            self.stdout.write(f'Avg. Sentiment Score: {sentiment.avg_sentiment_score}')
            self.stdout.write(f'Avg. Word Count: {sentiment.avg_word_count}')
            
            # Display word cloud URLs if they exist
            # Assuming you will add these fields later, or adjust based on actual fields in your model
            # For now, these are placeholders
            # self.stdout.write(f'Keywords Wordcloud: {sentiment.keywords_wordcloud if sentiment.keywords_wordcloud else "None"}')
            # self.stdout.write(f'Named Entities Wordcloud: {sentiment.named_entities_wordcloud if sentiment.named_entities_wordcloud else "None"}')
            # self.stdout.write(f'Nouns Wordcloud: {sentiment.nouns_wordcloud if sentiment.nouns_wordcloud else "None"}')
            # self.stdout.write(f'Verbs Wordcloud: {sentiment.verbs_wordcloud if sentiment.verbs_wordcloud else "None"}')
            # self.stdout.write(f'Adjectives Wordcloud: {sentiment.adjectives_wordcloud if sentiment.adjectives_wordcloud else "None"}')
            self.stdout.write(self.style.SUCCESS('-' * 50))
