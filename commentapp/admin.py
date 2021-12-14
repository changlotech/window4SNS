from django.contrib import admin
from commentapp.models import Comment, SubComment

admin.site.register(Comment)
admin.site.register(SubComment)
