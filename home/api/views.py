from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Article
from .serializers import ArticleSerializer


@api_view(['GET'])
def article_list(request):
    if request.method == "GET":
        query = Article.objects.all()
        serializer = ArticleSerializer(query, many=True)
        return Response(serializer.data)


@api_view(['PUT'])
def api_article_update(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['anjam shod'] = "update anjam shod"
            return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def api_article_delete(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {}
    if request.method == "DELETE":
        article.delete()
        data['hazf shod'] = "hazf anjam shod"
        return Response(data=data)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
def api_article_create(request):
    data = {}
    if request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data['anjam shod'] = "task jadidi sakhte shod"
            return Response(data=data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
