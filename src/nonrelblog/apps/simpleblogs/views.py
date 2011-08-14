# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/02
#
# To disable guest account create/update and 
# delete action, uncomments commented out lines below.
#
from django.core.urlresolvers import reverse
#from django.contrib.auth.decorators import permission_required
#from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from models import Article
from forms import ArticleForm


# -- list/detail
class ArticleListView(ListView):
    queryset = Article.objects.published()
    
class ArticleDetailView(DetailView):
    queryset = Article.objects.published()

# -- create/update/delete
class CreateArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    
#    @method_decorator(permission_required('simpleblogs.add_article'))
#    def dispatch(self, *args, **kwargs):
#        return super(CreateArticleView, self).dispatch(*args, **kwargs)
    
class UpdateArticleView(UpdateView):
    model = Article
    form_class = ArticleForm
    
#    @method_decorator(permission_required('simpleblogs.change_article'))
#    def dispatch(self, *args, **kwargs):
#        return super(UpdateArticleView, self).dispatch(*args, **kwargs)
    
class DeleteArticleView(DeleteView):
    model = Article
    
    def get_success_url(self):
        return reverse('simpleblogs_article_list')
    
#    @method_decorator(permission_required('simpleblogs.delete_article'))
#    def dispatch(self, *args, **kwargs):
#        return super(DeleteArticleView, self).dispatch(*args, **kwargs)