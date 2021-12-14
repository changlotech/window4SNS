from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.decorators import project_ownership_required
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project

    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def form_valid(self, form):
        temp_project = form.save(commit=False)
        temp_project.writer = self.request.user
        temp_project.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(project_ownership_required, 'get')
@method_decorator(project_ownership_required, 'post')
class ProjectUpdateView(UpdateView):
    model = Project
    context_object_name = 'target_project'
    form_class = ProjectCreationForm
    template_name = 'projectapp/update.html'

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

# 여러가지 object 들을 다룰수있게 만들어주는 MultipleObjectMixin
class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    # 템플릿 안에서 어떤이름으로 오브젝트를 다룰 것인지
    context_object_name = 'target_project'
    # 어떤 템플릿을 사용하는지지
    template_name = 'projectapp/detail.html'

    paginate_by = 25


    def get_context_data(self, **kwargs):

        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)
        else:
            subscription = None
        # get_object() 는 특정 pk 값을 갖는 object 를 가져오는 메소드 여기서는 Project 중에서 디테일페이제 있는 특정 Project 를 의미
        object_list = Article.objects.filter(project= self.get_object()).order_by('-pk')

        # 특정 pk 값을 가지고 있는 유일한 Project 객체에 딸려있는 Article 들을 필터링해서 projectapp/detail.html 에 찍어냄
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                               subscription=subscription,
                                                               **kwargs)

class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25