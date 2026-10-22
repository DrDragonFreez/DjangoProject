from django.conf import settings
from django.db import models


class Article(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    text = models.TextField("Текст статьи")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Автор",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        ordering = ["-created_at", "id"]
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def __str__(self):
        return self.title

    def get_short_text(self):
        if len(self.text) <= 300:
            return self.text
        return self.text[:300].rsplit(" ", 1)[0].rstrip() + "…"


class Comment(models.Model):
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        verbose_name="Статья"
    )
    name = models.CharField(max_length=100, verbose_name="Имя")
    comment = models.TextField(max_length=400, verbose_name="Комментарий")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    class Meta:
        ordering = ['created_on']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return self.comment[:60]