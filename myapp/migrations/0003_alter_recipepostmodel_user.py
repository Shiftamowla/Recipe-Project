# Generated by Django 5.1.2 on 2024-10-20 04:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_recipepostmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipepostmodel',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
