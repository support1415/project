from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseNotAllowed
from django.utils import timezone

from ..forms import CommentForm
from ..models import Article, Comment

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

def comment_modify(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.modified_at = timezone.now()
            comment.save()
            return redirect('projectsite:detail', article_id=comment.article.id)
    else:
        form = CommentForm(instance=comment)
    context = {'comment': comment, 'form': form}
    return render(request, 'comment_form.html', context)

def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('projectsite:detail', comment.article.id)

