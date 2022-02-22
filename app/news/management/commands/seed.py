from django.core.management.base import BaseCommand
from news.models import Article, Journalist
from .data import article_data, journalist_data


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
    first_journalist = Journalist.objects.first()
    first_id = first_journalist.id

    for x in range(0, len(article_data)):
        pk = first_id + x
        author = Journalist.objects.get(pk=pk)
        data = article_data[x]
        article = Article.objects.create(author=author, **data)
        article.save()

        print(f"{article.title} created...")
