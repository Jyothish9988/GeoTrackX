# Generated by Django 5.0.2 on 2024-02-16 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='admin_reply',
            field=models.TextField(blank=True),
        ),
    ]
