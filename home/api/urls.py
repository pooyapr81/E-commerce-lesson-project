from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('article/<int:pk>/update', views.api_article_update, name="article-update"),
    path('article/<int:pk>/delete', views.api_article_delete, name="article-delete"),
    path('article/create', views.api_article_create, name='article-create')
]