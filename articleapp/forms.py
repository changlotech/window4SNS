from django.forms import ModelForm
from django import forms
from django_summernote.widgets import SummernoteWidget

from articleapp.models import Article
from projectapp.models import Project





class ArticleCreationForm(ModelForm):

    # widget 속성으로 만들어질폼에 클래스랑, 스타일등을 미리결정해 줄 수 있다. height 는 auto ! 높이가 자동으로 커짐

    # 포린키로 연결될 Project 객체를 선택하기 위해서 사용하는 필드인데 queryset 은 필수요소다.
    # required=False 는 필수칸이 아님을 명시하기위해서 작성성



    class Meta:
        model = Article
        # project 필드는 해당 아티클이 어느 프로젝트에 소속된  것인지 입력하는 필드
        fields = ['title', 'image', 'content']

        labels = {
            'title': '제목',
            'image': '썸네일',
            'content': '내용'
        }

        widgets = {
            'content': SummernoteWidget(),
        }

