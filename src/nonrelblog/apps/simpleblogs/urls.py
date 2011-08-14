# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/02/27
#
from django.conf.urls.defaults import url, patterns

from views import CreateArticleView
from views import UpdateArticleView
from views import DeleteArticleView
from views import ArticleListView
from views import ArticleDetailView

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='simpleblogs_article_list'),
    url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='simpleblogs_article_detail'),
    url(r'^create/$', CreateArticleView.as_view(), name='simpleblogs_article_create'),
    url(r'^update/(?P<pk>\d+)/$', UpdateArticleView.as_view(), name='simpleblogs_article_update'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteArticleView.as_view(), name='simpleblogs_article_delete'),
)