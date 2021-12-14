from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    # 유저 객체랑 1대1관게, 유저객체 삭제되면 같이삭제, 유저객체에서 profile 로 객체접근연산자 사용할 수 있음
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 이미지가 저장되면 media/profile/ 에 저장
    image = models.ImageField(upload_to='profile/', null=True)
    # 닉네임 유일해야함
    nickname = models.CharField(max_length=20, unique=True, null=True)
    # 프로필 대화명 같으거
    message = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nickname

