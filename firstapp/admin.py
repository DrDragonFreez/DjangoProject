from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0
    fields = ("name", "comment", "created_on")
    readonly_fields = ("created_on",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ("title", "user", "text")
    readonly_fields = ("created_at",)

    list_display = ("id", "title", "user", "created_at")
    list_editable = ("title",)
    search_fields = ("title", "text")
    list_filter = ("created_at", "user")
    ordering = ("-created_at",)
    list_per_page = 10
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "article", "short_comment", "created_on")
    search_fields = ("name", "comment")
    list_filter = ("created_on", "article")
    ordering = ("-created_on",)
    list_editable = ("name",)
    list_per_page = 20

    @admin.display(description="Комментарий")
    def short_comment(self, obj):
        return obj.comment[:50] + ("..." if len(obj.comment) > 50 else "")