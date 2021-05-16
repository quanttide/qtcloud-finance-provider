# -*- coding: utf-8 -*-
"""
普通日记账（GeneralJournal）和普通分类账（GeneralLedger）数据模型。

数据模型设计：
- 日记账模型本身不包含借贷记录，借贷记录在分类账模型里，通过外键匹配和序列化类处理对视图层提供单条日记账的完整记录。
- 发生时间以日记账记录为准。（TODO）日记账时间的生成规则将会在原始凭证记录到日记账的过程中规定。

设计的出发点：
- 提高数据一致性。日记账的借贷记录需要进一步分类到分类账中，两步财务流程所需的数据只需要存一个即可。
- 提高可拓展性。一笔日记账可能包括不止一笔借（Debit）和贷（Credit），借贷记录（同时即分类账记录）单独存有利于拓展对异常（abnormal）记录的支持。
"""

import uuid
from django.db import models
from .accounts import Account


# ----- 日记账 -----

class GeneralJournal(models.Model):
    """
    普通日记账（不包含借贷记录）数据模型。
    """
    journal_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='日记账ID')
    occurrence_datetime = models.DateTimeField(verbose_name='发生时间')
    description = models.CharField(max_length=128, verbose_name='事件描述')
    is_adjustment = models.BooleanField(default=False, verbose_name='是否为调整账目')

    class Meta:
        verbose_name = '普通日记账'


# ----- 分类账 ------

class GeneralLedger(models.Model):
    """
    普通分类账/普通日记账的借贷记录的数据模型。
    """
    ledger_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='分类账ID')
    journal = models.ForeignKey(GeneralJournal, verbose_name='日记账')
    account = models.CharField(max_length=4, choices=Account.choices, verbose_name='会计科目')
    description = models.CharField(max_length=128, verbose_name='事件描述')
    debit_or_credit = models.CharField(verbose_name='借或贷')
    amount = models.DemicalField(max_digits=16, decimal_places=2, verbose_name='金额')

    class Meta:
        verbose_name = '普通分类账'


