from django.contrib import admin

from .models import Article, Comment, Ad, Category


admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Ad)