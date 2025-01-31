from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100, unique=True)
    summery = models.TextField()
    slug = models.SlugField()
    Author = models.TextField()
    master = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.slug} - {self.created}'

    def get_absolute_url(self):
        return reverse('home:postdetail', args=(self.id, self.slug))
