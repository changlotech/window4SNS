from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from articleapp.models import Article
from commentapp.decorators import comment_ownership_required
from commentapp.fomrs import CommentCreationForm, SubCommentCreationForm
from commentapp.models import Comment, SubComment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        temp_comment = form.save(commit=False)
        # 인풋타입히든의 value 얻음
        temp_comment.article = Article.objects.get(pk=self.request.POST['article_pk'])
        temp_comment.writer = self.request.user
        temp_comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})
    # self.object 에서 object 는 Comment

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentDeleteView(DeleteView):
    model = Comment
    context_object_name = 'target_comment'
    template_name = 'commentapp/delete.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})

@method_decorator(comment_ownership_required, 'get')
@method_decorator(comment_ownership_required, 'post')
class CommentUpdateView(UpdateView):
    model = Comment
    context_object_name = 'target_comment'
    form_class = CommentCreationForm
    template_name = 'commentapp/update.html'


    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})





class SubCommentCreateView(CreateView):
    model = SubComment
    form_class = SubCommentCreationForm
    template_name = 'commentapp/detail.html'

    def form_valid(self, form):
        temp_subcomment = form.save(commit=False)
        # 인풋타입히든의 value 얻음
        temp_subcomment.comment = Comment.objects.get(pk=self.request.POST['commnet_pk'])
        temp_subcomment.writer = self.request.user
        temp_subcomment.save()
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.comment.article.pk})














