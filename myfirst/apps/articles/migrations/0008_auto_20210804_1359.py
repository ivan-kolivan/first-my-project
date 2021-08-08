# Generated by Django 3.1.2 on 2021-08-04 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_category_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='buy_link',
            field=models.URLField(max_length=100, verbose_name='Ссылка на товар'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articles.category', verbose_name='Рубрика'),
        ),
    ]
