from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    datetime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text

class Entry(models.Model):
    """Информация по теме"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text[:50] + '...'

