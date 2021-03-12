# Generated by Django 3.1.6 on 2021-03-03 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20210214_0231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AddField(
            model_name='tags',
            name='article',
            field=models.ManyToManyField(to='Blog.Article'),
        ),
    ]