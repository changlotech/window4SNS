from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm

    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        # DB 에 저장하기전에 잠깐 멈춤
        temp_profile = form.save(commit=False)
        # 프로필객체의 user 필드를 채우자
        temp_profile.user = self.request.user
        # 채웠으니 저장
        temp_profile.save()
        # 다시 form_valid 가 정의해둔대로 동작
        return super().form_valid(form)
    # accountapp:detail 로 이동할때는 pk 값이 필요하니까  아래와 같이 작성 self.object 는 Profile
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm

    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})