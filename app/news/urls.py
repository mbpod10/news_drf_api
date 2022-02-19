from django.urls import path
from .function_views import article_list_view, article_detail_view
from .class_views import ArticleList, ArticleDetailView
urlpatterns = [
    path('articles/', article_list_view),
    path('articles/<int:pk>', article_detail_view),
    path('articles_/', ArticleList.as_view()),
    path('articles_/<int:pk>', ArticleDetailView.as_view()),
]
