from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Article, Journalist
from .serializers import ArticleSerializer, JournalistSerializer


@api_view(['GET', 'POST'])
def article_list_view(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_view(request, pk=None):
    try:
        article = Article.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({"error": "Article does not exist"}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def journalist_list_view(request):
    if request.method == 'GET':
        journalists = Journalist.objects.all()
        serializer = JournalistSerializer(journalists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
