from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=300, null=True)
