from django.core.management.base import BaseCommand
from news.models import Article
from .data import seed_data


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Seed Data...')
        self.stdout.write("Deleting data...")
        clear_data()
        self.stdout.write("Creating data...")
        create_articles(seed_data=seed_data)


def clear_data():
    Article.objects.all().delete()


def create_articles(seed_data):
    for object in seed_data:
        article = Article.objects.create(**object)
        article.save()
        print(f"{article.title} created...")
