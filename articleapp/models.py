from django.contrib.auth.models import User
from django.db import models
from projectapp.models import Project
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



class Article(models.Model, HitCountMixin):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, related_name='article', null=True, blank=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)

    def __str__(self):
        return self.title
