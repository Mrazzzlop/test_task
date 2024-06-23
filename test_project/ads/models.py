from django.db import models


class Advertisement(models.Model):
    """Модель объявления"""
    title = models.CharField(max_length=255)
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=100)
    views = models.IntegerField()
    position = models.IntegerField()


class User(models.Model):
    """Модель пользователя"""
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
