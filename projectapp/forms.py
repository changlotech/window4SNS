from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields= ['image', 'title', 'description']

# 위치, 상태의 변화와 관련있음 == meta

