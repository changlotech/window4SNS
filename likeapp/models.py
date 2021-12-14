from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article

# 연관된 모델필드명이랑 related_name 의 값이 겹치면 안 됨.
class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_record')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='like_record')


    class Meta:
        unique_together = ('user', 'article')

