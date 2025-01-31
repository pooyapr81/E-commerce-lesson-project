from django.shortcuts import render, redirect
from django.views import View
from .forms import formcreatupdate, ArticleSearchForm
from .models import Article


class HomeView(View):
    form_class = ArticleSearchForm

    def get(self, request):
        articles = Article.objects.all()
        if request.GET.get('search'):
            articles = articles.filter(body__contains=request.GET['search'])
        return render(request, 'home/index.html', {'articles': articles, 'form': self.form_class})

    def post(self, request):
        return render(request, 'home/index.html')


class ArticleView(View):
    form_class = ArticleSearchForm

    def get(self, request):
        articles = Article.objects.all()
        if request.GET.get('search'):
            articles = articles.filter(body__contains=request.GET['search'])
        return render(request, 'home/articles.html', {'articles': articles, 'form': self.form_class})

    def post(self, request):
        return render(request, 'home/articles.html')


class AboutView(View):


    def get(self, request):

        return render(request, 'home/about.html')

    def post(self, request):
        return render(request, 'home/about.html')