from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from ..forms import ArticleForm
from ..models import Article

@login_required(login_url='common:login')
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.created_at= timezone.now()
            article.save()
            return redirect('projectsite:index')
    else:
        form = ArticleForm()
    context = {'form': form}
    return render(request, 'article_form.html', context)

def article_modify(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.modified_at = timezone.now()
            article.save()
            return redirect('projectsite:detail', article_id=article.id)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form}
    return render(request, 'article_form.html', context)

def article_delete(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    return redirect('projectsite:index')

def article_vote(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.voter.add(request.user)
    return redirect('projectsite:detail', article_id=article.id)