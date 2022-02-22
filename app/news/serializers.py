from datetime import datetime
from django.utils.timesince import timesince
from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    time_since_publication = serializers.SerializerMethodField()

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
                "The title has to be at least 60 chars long")
        return value
