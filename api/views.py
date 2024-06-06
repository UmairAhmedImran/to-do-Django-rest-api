from rest_framework import generics, mixins, authentication, permissions
from .models import Todo
from .serializers import TodoSerializer
from .permission import isTodoEditor


class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAdminUser, isTodoEditor]
    authentication_classes = [authentication.SessionAuthentication]


class TodoRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class TodoMixin(generics.GenericAPIView,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.DestroyModelMixin,
                mixins.UpdateModelMixin,
                mixins.CreateModelMixin):

    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = "pk"

    permission_classes = [permissions.IsAdminUser, isTodoEditor]
    authentication_classes = [authentication.SessionAuthentication]

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
