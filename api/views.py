from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .mixins import TodoEditorPermissionMixin
from . import client


class TodoListCreateAPIView(TodoEditorPermissionMixin,
                            generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoRetrieveUpdateDelete(TodoEditorPermissionMixin,
                               generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class get_view(generics.ListAPIView, TodoEditorPermissionMixin):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'

# retrieve_view = TodoRetrieveUpdateDelete({'get': 'retrieve'})


class TodoMixin(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.CreateModelMixin,
                TodoEditorPermissionMixin):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def perform_update(self, serializer):
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


class SearchListView(generics.GenericAPIView):
    def get(self, request,  *args, **kwatgs):
        if not request.user.is_authenticated:
            return Todo.objects.none()
        query = []
        tags = []

        query = request.GET.get('q')
        tags = request.GET.get('tag')

        if not query:
            return Response("", status=400)

        result = client.perform_search(query, tags=tags)

        return Response(result)
