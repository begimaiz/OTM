from django.db import models


class Task(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('description', max_length=150)

    def __str__(self):
        return self.title
