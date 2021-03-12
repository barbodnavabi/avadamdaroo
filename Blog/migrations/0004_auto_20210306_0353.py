# Generated by Django 3.1.6 on 2021-03-06 11:53

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_auto_20210303_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='description',
            new_name='description_en',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='title',
            new_name='title_en',
        ),
        migrations.AddField(
            model_name='article',
            name='description_fa',
            field=ckeditor_uploader.fields.RichTextUploadingField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='description_tr',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_fa',
            field=models.CharField(default=1, max_length=200, verbose_name='عنوان مقاله'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_tr',
            field=models.CharField(default=1, max_length=200, verbose_name='عنوان مقاله'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='title_fa',
            field=models.CharField(default=1, max_length=200, verbose_name='عنوان دسته\u200cبندی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tags',
            name='title_tr',
            field=models.CharField(default=1, max_length=200, verbose_name='عنوان دسته\u200cبندی'),
            preserve_default=False,
        ),
    ]