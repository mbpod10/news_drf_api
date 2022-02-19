from django.urls import path
from .views import article_list_view
urlpatterns = [
    path('articles/', article_list_view),
]
