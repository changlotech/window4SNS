from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        # 참고할 모델
        model = Profile
        # 어떤필드를 입력폼으로 받을것인가
        fields = ['image', 'nickname', 'message']