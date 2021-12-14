from django.urls import path
from . import views

app_name = 'commentapp'

urlpatterns = [
    path('create/', views.CommentCreateView.as_view(), name='create'),
    path('delete/<int:pk>', views.CommentDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', views.CommentUpdateView.as_view(), name='update'),
    path('subcreate/', views.SubCommentCreateView.as_view(), name='subcreate'),
]
