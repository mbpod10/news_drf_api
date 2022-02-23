from .models import Article
from .serializers import ArticleViewSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


class ArticleList(APIView):

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleViewSerializer(articles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ArticleViewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailView(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk=pk)
        serializer = ArticleViewSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        article = self.get_object(pk=pk)
        serializer = ArticleViewSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk=pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
