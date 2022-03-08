from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category


def home(request, page=1):
    article_list = Article.objects.published()
    paginator = Paginator(article_list, 2)  # Show 5 article per page.
    articles = paginator.get_page(page)
    context = {
        "articles": articles
    }
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    context ={
        'article': get_object_or_404(Article, slug=slug, status='p')
    }
    return render(request, 'blog/detail.html', context)


def category(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug, status=True)
    article_list = category.articles.published()
    paginator = Paginator(article_list, 2)  # Show 5 article per page.
    articles = paginator.get_page(page)
    context = {

        'articles': articles,
        'category': category
    }
    return render(request, 'blog/category.html', context)
