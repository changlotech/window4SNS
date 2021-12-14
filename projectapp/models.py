from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='project', null=True, blank=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'

    def get_absolute_url(self):
        return f'/projects/{self.pk}/'

