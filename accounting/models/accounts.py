# -*- coding: utf-8 -*-
"""
会计科目数据模型。

会计科目标准：暂时遵循Wild等著《Fundamental Accounting Principles》第21版的会计科目设立。

技术实现：暂时采用硬编码的方式以枚举类型实现，SaaS化时可考虑可导入模式。详见
  - https://docs.djangoproject.com/en/3.1/howto/initial-data/
"""

from django.db import models


class Account(models.TextChoices):
    """
    会计科目数据模型。
    """
    CASH = '101', '现金'
    ACCOUNTS_RECEIVABLE = '106', '应收账款'
    SUPPLIES = '126', '原料'
    EQUIPMENT = '167', '固定资产'
    ACCOUNTS_PAYABLE = '201', '应付账款'
    SALARIES_PAYABLE = '206', '应付薪资'
    UNEARNED_CONSULTING_REVENUE = '236', '未获得咨询收入'
    CONSULTING_REVENUE = '403', '咨询收入'
    DEPRECIATION_EXPENSE = '612', '设备折旧费用'
    SALARIES_EXPENSE = '622', '薪资支出'
    RENT_EXPENSE = '640', '租金支出'
    SUPPLIES_EXPENSE = '652', '原料支出'
    UTILITIES_EXPENSE = '690', '水电费'
