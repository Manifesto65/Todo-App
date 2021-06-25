from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    STATUS_CHOICES = [
        ('P', 'PENDING'),
        ('C', 'COMPLETED'),
    ]
    PRIORITY_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    title = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    @staticmethod
    def get_all_todos(user):
        return Todo.objects.filter (user = user).order_by('priority')

    @staticmethod
    def delete_todo(id):
        return Todo.objects.filter(id = id).delete()

    @staticmethod
    def change_todo_status(id, status):
        todo = Todo.objects.get(id=id)
        todo.status = status
        todo.save()
        return True