from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Article, Journalist


class ArticlePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = "__all__"


class ArticleViewSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Article
        fields = ("id", "author", "title", "description", "body",
                  "location", "publication_date", "active",
                  "created_at", "updated_at", "time_since_publication")

    def get_time_since_publication(self, object):
        publication_date = object.publication_date
        now = datetime.now()
        time_delta = timesince(publication_date, now)
        return time_delta

    def validate(self, data):
        """Check if title and description are the same"""
        if data['title'] == data['description']:
            raise serializers.ValidationError(
                "Title and Description Must Be Different")
        return data

    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(
                "The title has to be at least 10 chars long")
        return value


class JournalistSerializer(serializers.ModelSerializer):

    articles = ArticleViewSerializer(many=True, read_only=True)
    article_count = serializers.SerializerMethodField()

    class Meta:
        model = Journalist
        fields = "__all__"

    def get_article_count(self, object):
        count = object.articles.count()
        return count
