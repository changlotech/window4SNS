from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required, 'get')
class SubscriptionView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        # GET 방식으로 보낸 요청중에서 project_pk 의 값을 얻어서 projectapp:detail 에 뿌려줌 즉 구독한 그 프로적트 디테일페이지에 리다이렉트
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})

    # get 함수 오버라이딩
    # Subscription 객체는 어떤 Project 에대한 구독인지, 그리고 그 프로젝트에대한 구독을 요청한 유저에 대한 정보를 담고있다.
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.request.GET.get('project_pk'))
        user = self.request.user
        # 특정 프로젝트에 대해서 user 가 구독을함 그 것을 subscription 변수에 담는다.
        subscription = Subscription.objects.filter(user=user, project=project)

        # 구독정보가 존재한다면 (구독중인상태)
        if subscription.exists():
            # 구독취소
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()
            # 구독정보가 존재하지 않는다면 (비구독중인 상태) 구독객체를 생성하는데 user 필드에는 구독을 요청한 유저로, 프로젝트 필드에는 특정 Project 객체로 채워서
        return super(SubscriptionView, self).get(request, *args, **kwargs)


@method_decorator(login_required, 'get')
class SubscriptionListView(ListView):
    model = Subscription
    context_object_name = 'subscription_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 30





@method_decorator(login_required, 'get')
class SubscriptionHotArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/hot_list.html'
    paginate_by = 5
    # 쿼리셋함수를 오버라이딩해서 가지고오는 게시글들의 조건을 바꿀 수 있다.
    def get_queryset(self):
        # 요청자의 모든 구독객체를 가져옴 근데 그 project 들을 list 화 시켜서 projects 변수에 담음
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        # 리스트화된 projects 들을 안에서 project 들을 필터링해서 나눔
        article_list = Article.objects.filter(project__in=projects)
        return article_list






