from django.db import models

# Create your models here.


class Article(models.Model):
    author = models.CharField(max_length=55)
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=120)
    body = models.TextField()
    location = models.CharField(max_length=55)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
