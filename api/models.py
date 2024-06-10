from django.db import models
from django.conf import settings
import random

user = settings.AUTH_USER_MODEL

tag = ["rook", "bishop", "queen"]


class Todo(models.Model):
    user = models.ForeignKey(user, default=1, null=True,
                             on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300, null=True)

    def get_tag(self):
        return [random.choice(tag), random.choice(tag), random.choice(tag)]
