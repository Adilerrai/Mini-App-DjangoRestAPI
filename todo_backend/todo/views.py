from rest_framework import viewsets
from .models import Todo, TodoList
from .serializers import TodoSerializer, TodoListDetailSerializer
from rest_framework.permissions import IsAuthenticated  


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes=(IsAuthenticated,)
    filterset_fields = ['done', 'due_date']

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListDetailSerializer