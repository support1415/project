from django.urls import path, include

from .views import base_views, article_views, comment_views, reply_views

app_name = 'projectsite'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:article_id>/',
         base_views.detail, name='detail'),

    # article_views.py
    path('article/create/',
         article_views.article_create, name='article_create'),
    path('article/modify/<int:article_id>/',
         article_views.article_modify, name='article_modify'),
    path('article/delete/<int:article_id>/',
         article_views.article_delete, name='article_delete'),

    # comment_views.py
    path('comment/create/<int:article_id>/',
         comment_views.comment_create, name='comment_create'),
    path('comment/modify/<int:comment_id>/',
         comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/<int:comment_id>/',
         comment_views.comment_delete, name='comment_delete'),

    # reply_views.py
    path('reply/create/<int:comment_id>/', 
         reply_views.reply_create, name='reply_create'),
    path('reply/modify/<int:reply_id>/', 
         reply_views.reply_modify, name='reply_modify'),
    path('reply/delete/<int:reply_id>/', 
         reply_views.reply_delete, name='reply_delete'),

    path('article/vote/<int:article_id>/', article_views.article_vote, name='article_vote'),
    path('comment/vote/<int:comment_id>/', comment_views.comment_vote, name='comment_vote'),
   
]