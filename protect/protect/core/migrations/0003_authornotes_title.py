# Generated by Django 4.1 on 2023-08-25 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_authornotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='authornotes',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
