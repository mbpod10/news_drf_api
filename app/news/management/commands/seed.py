from django.core.management.base import BaseCommand
from news.models import Article, Journalist
from .data import article_data, journalist_data
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('Processing Seed Data...')
        self.stdout.write("Deleting Journalists & Articles...")
        clear_data()
        self.stdout.write("Creating Journalists...")
        create_journalists()
        self.stdout.write("Creating Articles...")
        create_articles()


def clear_data():
    Article.objects.all().delete()
    Journalist.objects.all().delete()


def create_journalists(data=journalist_data):
    for person in data:
        journalist = Journalist.objects.create(**person)
        journalist.save()


def create_articles(article_data=article_data):
    first_id = Journalist.objects.first().id
    last_id = Journalist.objects.last().id
    range_id = list(range(first_id, last_id+1))

    for x in range(0, len(article_data)):
        pk = random.choice(range_id)
        author = Journalist.objects.get(pk=pk)
        data = article_data[x]
        article = Article.objects.create(author=author, **data)
        article.save()

        print(f"{article.title} created...")
