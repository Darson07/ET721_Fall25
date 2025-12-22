from django.db import models

class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Personal', 'Personal'),
        ('Deadline', 'Deadline'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
