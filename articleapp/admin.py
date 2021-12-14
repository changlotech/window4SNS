from django.contrib import admin
from articleapp.models import Article
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
    search_fields = ['title']
    summernote_fields = '__all__'

admin.site.register(Article, SummernoteModelAdmin)
