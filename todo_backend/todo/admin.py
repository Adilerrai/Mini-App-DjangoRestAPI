from django.contrib import admin
from .models import Todo, TodoList



class TodoInLine(admin.TabularInline):
    model = Todo
    extra = 3

@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display=['name']
    inlines = (TodoInLine,)


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'list')
    list_filter = ('due_date',)
    search_fields = ('title', 'due_date')