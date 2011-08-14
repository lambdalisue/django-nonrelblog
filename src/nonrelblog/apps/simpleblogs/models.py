# -*- coding: utf-8 -*-
#
# Author:        alisue
# Date:            2011/01/03
#
from django.db import models
from django.utils.text import ugettext_lazy as _

from datetime import date

class ArticleManager(models.Manager):
    u"""Manager of Article Model"""
    def published(self):
        u"""Return non draft article queryset"""
        return self.filter(is_draft=False)
    
    def draft(self):
        u"""Return draft article queryset"""
        return self.filter(is_draft=True)
    
class Article(models.Model):
    u"""Blog article model"""
    is_draft        = models.BooleanField(_('is draft'), default=False, help_text=_('Check this for saving article as draft.'))
    title           = models.CharField(_('title'), max_length=100, default=_('No title'))
    body            = models.TextField(_('body'))
    
    enable_comments = models.BooleanField(_('enable comments'), default=True)
    # Automatically
    publish_at      = models.DateField(_('date published'), null=True, editable=False)
    created_at      = models.DateTimeField(_('date time created'), auto_now=True)
    updated_at      = models.DateTimeField(_('date time updated'), auto_now_add=True)
    
    objects         = ArticleManager()
    
    class Meta:
        get_latest_by       = ('updated_at',)
        ordering            = ('title',)
        unique_together     = ('title', 'publish_at')
        verbose_name        = _('article')
        verbose_name_plural = _('articles')
        
    def __unicode__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        if self.is_draft:
            return ('simpleblogs_article_update', (), {'pk': self.pk})
        else:
            return ('simpleblogs_article_detail', (), {'pk': self.pk})
    
    def clean(self, **kwargs):
        if self.is_draft and self.publish_at:
            self.publish_at = None
        elif not self.is_draft and not self.publish_at:
            self.publish_at = date.today()
        super(Article, self).clean(**kwargs)
        
    def validate_unique(self, exclude=None):
        if isinstance(exclude, (list, tuple)):
            if 'publish_at' in exclude: exclude.remove('publish_at')
        super(Article, self).validate_unique(exclude)
    
from django.contrib.comments.moderation import CommentModerator, moderator, AlreadyModerated
class ArticleModerator(CommentModerator):
    email_notification = False
    enable_field = 'enable_comments'
try:
    moderator.register(Article, ArticleModerator)
except AlreadyModerated:
    pass
