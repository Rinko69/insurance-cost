import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from insurance_cost.models import Rate

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'loading rates from data in json or csv'

    def add_arguments(self, parser):
        parser.add_argument('filename', default='rates.csv', nargs='?',
                            type=str)

    def handle(self, *args, **options):
        try:
            with open(os.path.join(DATA_ROOT, options['filename']), 'r',
                      encoding='utf-8') as f:
                datareader = csv.reader(f)
                for row in datareader:
                    Rate.objects.get_or_create(
                        name=row[0],
                        slug=row[1]
                    )
        except FileNotFoundError:
            raise CommandError('Добавьте файл rates в директорию data')
