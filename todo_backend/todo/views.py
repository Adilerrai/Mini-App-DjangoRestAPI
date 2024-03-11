from rest_framework import viewsets
from .models import Todo, TodoList
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, TodoSerializer, TodoListDetailSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes=(IsAuthenticated,)
    filterset_fields = ['done', 'due_date']

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListDetailSerializer