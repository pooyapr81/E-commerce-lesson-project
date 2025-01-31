from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'slug', 'updated')
    search_fields = ('user', 'title', 'slug', 'body')
    list_filter = ('created', 'updated')
    prepopulated_fields = {'slug': ('summery',)}
    raw_id_fields = ('user',)


admin.site.register(Article, ArticleAdmin)
