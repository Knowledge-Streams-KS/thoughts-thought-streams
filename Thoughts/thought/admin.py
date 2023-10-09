from django.contrib import admin
from . models import Thought, Comment
# Register your models here.

@admin.register(Thought)
class ThoughtAdmin(admin.ModelAdmin):
    list_display = ['id','title','content', 'author', 'created_at', 'is_private']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','text','time', 'thought', 'user']