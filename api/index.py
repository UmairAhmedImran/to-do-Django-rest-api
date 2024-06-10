import algoliasearch_django as algoliasearch
from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Todo


@register(Todo)
class TodoIndexer(AlgoliaIndex):
    fields = [
        "title",
        "content"
    ]

    settings = {
        'searchableAttributes': ['title', 'content']
    }

    tags = "get_tag"
