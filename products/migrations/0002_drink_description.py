# Generated by Django 4.0.5 on 2022-07-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
