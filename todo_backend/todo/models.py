from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=255)
    due_date = models.DateField()
    completed = models.BooleanField(default=False)
    favourite = models.BooleanField(default=False)


    list = models.ForeignKey('TodoList',null=False, on_delete=models.CASCADE)
    

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)



    class Meta:
        verbose_name = 'Todo List'
        verbose_name_plural = 'Todo Lists'
