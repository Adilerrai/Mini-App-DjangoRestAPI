# Generated by Django 5.0.3 on 2024-03-10 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todolist_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='done',
        ),
    ]
