from django.db import models

# Create your models here.


class ClientScore(models.Model):
    """
    客户端分数记录
    """
    client_name = models.CharField(max_length=20, verbose_name=u"客户端名称")
    score = models.PositiveIntegerField(verbose_name=u"分数", default=0)
