# -*- coding:utf-8 -*-

from django.db import models


# ----- 原始凭证 -----

class SourceDocument(models.Model):
    class Meta:
        verbose_name = '原始凭证'


# ----- 分类日记账 -----

class SpecificJournal(models.Model):
    class Meta:
        verbose_name = '分类日记账'
