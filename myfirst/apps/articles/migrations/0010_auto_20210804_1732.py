# Generated by Django 3.1.2 on 2021-08-04 14:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_auto_20210804_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
