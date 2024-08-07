from django.core.management.base import BaseCommand
from api.models import Company

class Command(BaseCommand):
    help = 'Display all company names and their corresponding IDs'

    def handle(self, *args, **options):
        companies = Company.objects.all().order_by('id')
        self.stdout.write(self.style.SUCCESS('Company ID | Company Name'))
        self.stdout.write(self.style.SUCCESS('-' * 30))
        for company in companies:
            self.stdout.write(f'{company.id:10} | {company.name}')
