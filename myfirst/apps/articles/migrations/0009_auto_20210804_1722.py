# Generated by Django 3.1.2 on 2021-08-04 14:22

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20210804_1359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'ordering': ['id'], 'verbose_name': 'Реклама', 'verbose_name_plural': 'Реклама'},
        ),
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
