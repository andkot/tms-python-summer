from django.db import models
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(max_length=5000)
    author_name = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def short_description(self):
        return truncatechars(self.description, 10)

    def __str__(self):
        return self.title
