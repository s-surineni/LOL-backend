from django.contrib.auth.models import User
from django.db import models


class List(models.Model):
    name = models.TextField()
    create_by = models.ForeignKey(
        User, related_name="creator", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    # tags


class Item(models.Model):
    name = models.TextField()
    url = models.URLField()
    lists = models.ManyToManyField(List)

    def __str__(self):
        return "{}:{}".format(self.name, self.url)

    # likes -> computed field?
    # comments


class Comment(models.Model):
    content = models.TextField()
    # comment by -> foreignkey


class Tag(models.Model):
    pass
