from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Article
from django.http import HttpResponseNotAllowed
from .forms import ArticleForm, CommentForm

def index(request):
    article_list = Article.objects.order_by('-created_at')
    context = {'article_list':article_list}
    return render(request, 'article_list.html', context)

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {'article': article}
    return render(request, 'article_detail.html', context)

def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.created_at = timezone.now()
            comment.article = article
            comment.save()
            return redirect('projectsite:detail', article_id=article.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'article': article, 'form': form}
    return render(request, 'article_detail.html', context)

def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.created_at= timezone.now()
            article.save()
            return redirect('projectsite:index')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'article_form.html', context)