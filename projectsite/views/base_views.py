from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import Article

def index(request):
    page = request.GET.get('page', '1')
    article_list = Article.objects.order_by('-created_at')
    paginator = Paginator(article_list, 10)
    page_obj = paginator.get_page(page)
    context = {'article_list': page_obj}
    return render(request, 'article_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'article_detail.html', context)