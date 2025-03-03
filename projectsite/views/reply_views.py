from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import ReplyForm
from ..models import Reply, Comment, Article

def reply_create(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.created_at = timezone.now()
            reply.comment = comment
            reply.save()
            return redirect('{}#reply_{}'.format(
                resolve_url('projectsite:detail', article_id=reply.comment.article.id), reply.id))
    else:
        form = ReplyForm()
    context = {'form': form}
    return render(request, 'reply_form.html', context)


def reply_modify(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    if request.method == "POST":
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.author = request.user
            reply.modified_at = timezone.now()
            reply.save()
            return redirect('{}#reply_{}'.format(
                resolve_url('projectsite:detail', article_id=reply.comment.article.id), reply.id))
    else:
        form = ReplyForm(instance=reply)
    context = {'form': form}
    return render(request, 'reply_form.html', context)


def reply_delete(request, reply_id):
    reply = get_object_or_404(Reply, pk=reply_id)
    reply.delete()
    return redirect('projectsite:detail', article_id=reply.comment.article.id)