from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDelete

urlpatterns = [
    path("", TodoListCreateAPIView.as_view()),
    path("updel/<int:pk>/", TodoRetrieveUpdateDelete.as_view())
]
