from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.edit import FormMixin

from articleapp.decorators import article_ownership_required
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article
from commentapp.fomrs import CommentCreationForm
from projectapp.models import Project
from hitcount.views import HitCountDetailView




@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.project = Project.objects.get(pk=self.request.POST['project_pk'])
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})



class ArticleDetailView(HitCountDetailView, FormMixin):
    model = Article
    form_class = CommentCreationForm
    context_object_name = 'target_article'
    template_name = 'articleapp/detail.html'
    count_hit = True


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreationForm
    template_name = 'articleapp/update.html'


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')


# 아티클리스트뷰

class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 30
    ordering = '-pk'

    def get_queryset(self):
        if self.request.GET['st'] == 'hot':
            article_list = Article.objects.all().order_by('-pk')
        elif self.request.GET['st'] == 'day':
            article_list = Article.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=1)).order_by('-like')
        elif self.request.GET['st'] == 'week':
            article_list = Article.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=7)).order_by('-like')
        elif self.request.GET['st'] == 'month':
            article_list = Article.objects.filter(created_at__gte=timezone.now() - timezone.timedelta(days=30)).order_by('-like')
        return article_list


class ArticleListViewMain(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 30
    ordering = '-pk'











