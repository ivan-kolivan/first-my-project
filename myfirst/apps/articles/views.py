from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Article, Comment, Ad, Category

latest_ad_list = Ad.objects.all()
# главная страница
def index(request):
	category = Category.objects.all()
	latest_articles_list = Article.objects.order_by('-pub_date')
	context = {
		'latest_articles_list': latest_articles_list,
		'latest_ad_list': latest_ad_list,
		'category': category
	}
	return render(request, 'list.html', context)


def by_category(request, category_id):
	current_category = Category.objects.get(pk = category_id)
	category = Category.objects.all()
	articles_list = Article.objects.filter(category = category_id)
	context = {
		'latest_articles_list': articles_list,
		'current_category':  current_category,
		'latest_ad_list': latest_ad_list,
		'category': category
	}
	
	return	render(request, 'articles/by_rubric.html', context)


# страница с подробностями
def detail(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
		a.article_views += 1
		a.save()
	except:
		return Http404()

	latest_comment_list = a.comment_set.order_by('-id')

	category = Category.objects.all()

	context = {
		'article': a, 
		'latest_comment_list': latest_comment_list, 
		'latest_ad_list': latest_ad_list,
		'category': category
	}

	return render(request, 'articles/detail.html', context)

# страница с комментариями
def leave_comment(request, article_id):
	try:
		a = Article.objects.get( id = article_id )
	except:
		return Http404()

	a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

	return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )