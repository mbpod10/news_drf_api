from django.urls import path
from .function_views import article_list_view, article_detail_view, journalist_list_view
from .class_views import ArticleList, ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('articles/', article_list_view, name="list"),
    path('articles/<int:pk>', article_detail_view, name="detail"),
    path('articles_/', ArticleList.as_view()),
    path('articles_/<int:pk>', ArticleDetailView.as_view()),
    path('articles_/<int:pk>', ArticleDetailView.as_view()),
    path('journalists/', journalist_list_view),
]
