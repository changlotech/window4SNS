from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from .decorators import account_ownership_required
from .forms import AccountUpdateForm, AccountCreationForm

has_ownership = [account_ownership_required, login_required]


class AccountCreateView(CreateView):
    # 유저라는 모델로 CreateView 를 만들것이다 (주요한 파라미터 4개)
    model = User
    # 그 유저모델을 만들기위한 폼은 UserCreationFrom 이라는 것을 이용할 것이다
    form_class = AccountCreationForm
    # 계정을 성공적으로 생성하면 리다이렉트할 위치 CBV 에서는 reverse_lazy 를 사용 FBV 에서는 reverse 를 하용
    success_url = reverse_lazy('home')
    # 회원가입을 할때 볼 html 은 어떤 template 파일을 쓸 것인지
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    # 어떤 모델을 쓸건지
    model = User
    # 어느 템플릿에 시각화해서 보여줄 건지
    template_name = 'accountapp/detail.html'
    # 모델 겍체의 이름을 변경하는 파라미터
    context_object_name = 'target_user'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    # AccountUpdateForm 이라고 내가 forms.py 에 정의한 커스터마이징 폼을 사용
    form_class = AccountUpdateForm
    success_url = reverse_lazy('home')
    # 정보수정을 할때 볼 html 은 어떤 template 파일을 쓸 것인지
    template_name = 'accountapp/update.html'
    context_object_name = 'target_user'


# @method_decorator(login_required, 'get')
# @method_decorator(login_required, 'post')
# @method_decorator(account_ownership_required, 'get')
# @method_decorator(account_ownership_required, 'post')

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    context_object_name = 'target_user'

