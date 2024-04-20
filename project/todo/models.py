from django.db import models


class TaskStatus(models.TextChoices):
    DONE = 'Done', 'Done'
    PENDING = 'Pending', 'Pending'


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=TaskStatus.choices,
        default=TaskStatus.PENDING,
    )

    def __str__(self):
        return f"Title ({self.title})"
