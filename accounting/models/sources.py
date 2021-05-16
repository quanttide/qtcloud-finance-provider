# -*- coding:utf-8 -*-
"""
原始凭证和原始收据。

原始凭证用于记录发票和收据等财务凭证；
原始收据用于记录企业员工财务事务相关记录，数据主要来自企业微信。
"""

import uuid
from django.db import models


# ----- 原始凭证 -----

class SourceDocumentType(models.TextChoices):
    INVOICE = 'invoice', '发票（或支出凭证）'
    CONTACT = 'contact', '合同（或合约凭证）'
    RECEIPT = 'receipt', '收据'


class SourceDocument(models.Model):
    """
    原始凭证类。

    主要来源于企业经营过程产生的收入和支出的原始凭证。
    """
    doc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='凭证ID')
    doc_type = models.FileField(verbose_name='凭证类型')
    occurrence_date = models.DateField(verbose_name='发生时间')
    amount = models.DemicalField(max_digits=16, decimal_places=2, verbose_name='金额')
    is_checked = models.BooleanField(default=False, verbose_name='是否核查')

    class Meta:
        verbose_name = '原始凭证'


# ----- 原始记录 -----

class SourceRecordType(models.TextChoices):
    REIMBURSEMENT = 'reimbursement', '报销'
    EXPENSE = 'expense', '费用'
    SALARY = 'salary', '薪酬'


class SourceRecord(models.Model):
    """
    原始记录。

    主要来源于企业微信等内部人员财务事件相关记录。
    """
    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='记录ID')
    record_type = models.CharField(max_length=16, choices=SourceRecordType.choices, verbose_name='记录类型')
    occurrence_date = models.DateField(verbose_name='发生时间')
    amount = models.DemicalField(max_digits=16, decimal_places=2, verbose_name='金额')
    is_edited = models.BooleanField(default=False, verbose_name='是否编辑过原始记录')

    source_document = models.ForeignKey(SourceDocument, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '原始记录'


# ----- 原始账单 -----

class BillAccount(models.TextChoices):
    pass


class SourceBill(models.Model):
    """
    原始账单。

    主要来源于银行账户的账单明细。
    """
    bill_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='账单ID')
    bill_account = models.CharField(max_length=16, choices=BillAccount.choices, verbose_name='现金账户')
    raw_bill_id = models.CharField(max_length=64, default=None, null=True, blank=True, verbose_name='现金账户的账单ID')
    occurrence_date = models.DateField(verbose_name='发生时间')
    amount = models.DemicalField(max_digits=16, decimal_places=2, verbose_name='金额')

    class Meta:
        verbose_name = '原始账单'


