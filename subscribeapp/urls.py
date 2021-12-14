from django.urls import path
from . import views

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/', views.SubscriptionView.as_view(), name='subscribe'),
    path('list/', views.SubscriptionListView.as_view(), name='list'),
    path('hotlist/', views.SubscriptionHotArticleListView.as_view(), name='hotlist'),
]