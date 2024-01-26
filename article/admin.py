from django.contrib import admin
from .models import Article, Comment


class ArticleAdmin(admin.TabularInline):
    model = Comment
    extra = 0

class CommentAdmin(admin.ModelAdmin):
    inlines = [ArticleAdmin]


admin.site.register(Article, CommentAdmin)
admin.site.register(Comment)