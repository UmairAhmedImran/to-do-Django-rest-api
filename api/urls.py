from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDelete, TodoMixin

urlpatterns = [
    path("", TodoListCreateAPIView.as_view()),
    path("updel/<int:pk>/", TodoRetrieveUpdateDelete.as_view()),
    path("list/", TodoMixin.as_view()),
    path("create/", TodoMixin.as_view()),
    path("delete/<int:pk>/", TodoMixin.as_view()),
    path("update/<int:pk>/", TodoMixin.as_view()),
    path("retrive/<int:pk>/", TodoMixin.as_view())
]
