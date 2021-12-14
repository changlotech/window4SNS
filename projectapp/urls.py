from django.urls import path
from . import views

app_name = 'projectapp'

# 뷰에대한 라우트 설정
urlpatterns = [
    path('list/', views.ProjectListView.as_view(), name='list'),
    path('create/', views.ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ProjectDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProjectUpdateView.as_view(), name='update'),
]