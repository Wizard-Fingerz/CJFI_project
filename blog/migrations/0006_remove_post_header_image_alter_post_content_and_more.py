# Generated by Django 4.0.3 on 2022-07-12 23:11

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_header_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='header_image',
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]