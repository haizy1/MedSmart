import csv
from django.conf import settings
from django.core.management.base import BaseCommand
from authentic.models import Symptomis

class Command(BaseCommand):
    help = "Loads symptoms data from CSV file"

    def handle(self, *args, **options):
        datafile = settings.BASE_DIR / 'authentic' / 'data' / 'symptoms.csv'

        with open(datafile) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                Symptomis.objects.get_or_create(name=row[0])