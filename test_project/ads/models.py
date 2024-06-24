from datetime import datetime, timezone, timedelta

from django.db import models
import uuid

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


class AuthToken(models.Model):
    key = models.CharField(max_length=40, primary_key=True)
    user = models.ForeignKey(User, related_name='auth_tokens', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
            self.expires_at = datetime.now(tz=timezone.utc) + timedelta(days=1)
        super().save(*args, **kwargs)

    def generate_key(self):
        return uuid.uuid4().hex
