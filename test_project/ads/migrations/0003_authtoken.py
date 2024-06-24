# Generated by Django 5.0.6 on 2024-06-24 08:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_tokens', to='ads.user')),
            ],
        ),
    ]
