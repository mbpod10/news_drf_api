from django.urls import path
from .views import article_list_view, article_detail_view
urlpatterns = [
    path('articles/', article_list_view),
    path('articles/<int:pk>', article_detail_view),
]
