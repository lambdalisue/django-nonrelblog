# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/02
#
from django import forms
from models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = (
            'title', 'is_draft', 'body','enable_comments',
        )