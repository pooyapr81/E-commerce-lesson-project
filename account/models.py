from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class Usertype(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField(null=True, blank=True)
    utype = models.ForeignKey(Usertype, on_delete=models.CASCADE, null=True, blank=True)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(receiver=create_profile, sender=User)
