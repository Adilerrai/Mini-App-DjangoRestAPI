from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password # Import the validate_password function
from rest_framework.validators import UniqueValidator # Import the UniqueValidator class
from todo.models import Todo, TodoList
from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TodoSerializer(serializers.ModelSerializer):

    dueDate = serializers.DateField(source='due_date')

    class Meta:
        model = Todo
        exclude = ['due_date']


class TodoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoList
        fields = '__all__'


class TodoListDetailSerializer(serializers.ModelSerializer):

    todos = TodoSerializer(source='todo_set', many=True)

    class Meta:
        model = TodoList
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email

        return token


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user