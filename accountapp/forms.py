from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class AccountCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(AccountCreationForm, self).__init__(*args, **kwargs)


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']

    def save(self, commit=True):
        user = super(AccountCreationForm, self).save(commit=False)
        user.save()
        return user


class AccountUpdateForm(AccountCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # UserCreationForm 이라는 장고가 만든 폼 전부다 상속받지만 딱하나 username 필드를 비활성화 시킴
        self.fields['username'].disabled = True




