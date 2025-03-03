from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

from django.utils import timezone
from django.contrib.auth.decorators import login_required

from ..forms import CommentForm
from ..models import Article, Comment

@login_required(login_url='common:login')
def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created_at = timezone.now()
            comment.article = article
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('projectsite:detail', article_id=comment.article.id), comment.id))
    else:
        form = CommentForm
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


def comment_vote(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.voter.add(request.user)
    return redirect('projectsite:detail', article_id=comment.article.id)

