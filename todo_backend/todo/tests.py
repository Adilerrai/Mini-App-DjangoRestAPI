from django.test import TestCase

from .models import Todo, TodoList



class TodoTestCase(TestCase):
    def setUp(self):
        self.todo_list = TodoList.objects.create(name="Test List")


    def test_something(self):
        pass
# Compare this snippet from todo-backend/todo/views.py:
    def test_create_todo(self):
        nbr_todo = Todo.objects.count()
        new_todo = Todo.objects.create(title="test", description="test", done=False, due_date="2022-12-12", list=self.todo_list)
        new_todo.save()
        self.assertEqual(Todo.objects.count(), nbr_todo + 1)