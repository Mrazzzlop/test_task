import json

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from ads.models import Advertisement


class Command(BaseCommand):
    """Команда импорта объявлений в базу данных."""
    help = 'Импорт объявлений из файла json'

    BASE_DIR = settings.BASE_DIR

    def handle(self, *args, **options):
        try:
            path = self.BASE_DIR / 'data/test_ads.json'
            with open(path, 'r', encoding='utf-8-sig') as file:
                data = json.load(file)
                for item in data:
                    Advertisement.objects.get_or_create(**item)
        except CommandError as error:
            raise CommandError from error

        self.stdout.write(self.style.SUCCESS('Данные успешно загружены'))
