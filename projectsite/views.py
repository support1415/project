from django.shortcuts import render, get_object_or_404
from .models import Article

def index(request):
    article_list = Article.objects.order_by('-created_at')
    context = {'article_list':article_list}
    return render(request, 'article_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'article_detail.html', context)