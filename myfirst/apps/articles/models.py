from django.db import models
from django.utils import timezone
import datetime

class Category(models.Model):
	name = models.CharField(max_length=50, verbose_name="Имя категории")
	icon = models.ImageField(verbose_name="Изображение категории товаров")

	def __str__(self) -> str:
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		ordering = ['id']

class Article(models.Model):
	category = models.ForeignKey("Category", null = True, on_delete=models.SET_NULL, verbose_name="Рубрика")
	article_title = models.CharField(max_length = 210, verbose_name='название статьи')
	article_text = models.TextField(verbose_name="содержимое статьи")
	pub_date = models.DateTimeField(verbose_name='дата публикации')
	article_views = models.IntegerField(verbose_name='Количестов просмотров статьи')
	image = models.ImageField(verbose_name="Изображение")
	buy_link = models.URLField(max_length = 100, verbose_name='Ссылка на товар')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'
		ordering = ['-pub_date']

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete = models.CASCADE)
	author_name = models.CharField(max_length = 50, verbose_name='имя автора')
	comment_text = models.CharField(max_length = 200, verbose_name='Текст комментария')

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'
		ordering = ['id']

class Ad(models.Model):
	html_code = models.TextField('HTML код рекламы') 

	class Meta:
		verbose_name = 'Реклама'
		verbose_name_plural = 'Реклама'
		ordering = ['id']