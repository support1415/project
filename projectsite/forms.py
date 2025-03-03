from django import forms
from django_summernote.widgets import SummernoteWidget
from projectsite.models import Article, Comment, Reply


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
        }
        labels = {
            'title': '제목',
            'content': '내용',
        }  

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'content': '답글내용'
        }
