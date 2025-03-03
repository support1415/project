from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')


    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='author_comment')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_comment')


class Reply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_reply')
    content = models.TextField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField(null=True, blank=True)
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.CASCADE)


