# Generated by Django 5.0.6 on 2024-05-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_user_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='adresse',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]