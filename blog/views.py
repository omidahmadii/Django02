from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    context ={
        'Articles': get_object_or_404(Article, status='p',).order_by('-publish')[:5]
    }
    return render(request, 'blog/home.html', context)


def detail(request, slug):
    context ={
        'Article': get_object_or_404(Article, slog=slug, status='p')
    }
    return render(request, 'blog/detail.html', context)
