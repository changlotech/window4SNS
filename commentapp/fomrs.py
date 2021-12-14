from django.forms import ModelForm

from commentapp.models import Comment, SubComment


class CommentCreationForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']




class SubCommentCreationForm(ModelForm):
    class Meta:
        model = SubComment
        fields = ['content']
        labels = {
            'content': '댓글'
        }
