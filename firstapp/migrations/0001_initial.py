from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


ARTICLES = [
    ("Как устроен современный сайт", "Сайт состоит из нескольких частей: структуры HTML, оформления CSS и интерактивного поведения JavaScript. Сервер принимает запрос, получает нужные данные и возвращает страницу браузеру. Django помогает организовать эту работу и связывает адреса, представления, шаблоны и базу данных."),
    ("Знакомство с Django", "Django — веб-фреймворк на языке Python. В проекте настройки и общие адреса находятся в конфигурации, а отдельные функции сайта удобно размещать в приложениях. Такой подход помогает развивать сайт по частям и повторно использовать готовые решения."),
    ("Зачем нужны модели", "Модель описывает данные сайта и правила их хранения. Например, модель статьи содержит заголовок, текст, автора и дату публикации. Django по модели создаёт таблицу базы данных с помощью миграций, а ORM позволяет работать с записями через объекты Python."),
    ("Шаблоны и адаптивная верстка", "Шаблон отвечает за HTML-разметку страницы и может показывать данные, переданные представлением. Bootstrap содержит готовые стили и компоненты, которые подстраивают сетку под ширину экрана. Благодаря этому меню и карточки остаются удобными на телефоне."),
]


def add_initial_articles(apps, schema_editor):
    Article = apps.get_model("firstapp", "Article")
    Article.objects.bulk_create([Article(title=title, text=text) for title, text in ARTICLES])


class Migration(migrations.Migration):
    initial = True
    dependencies = [("auth", "0012_alter_user_first_name_max_length")]
    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200, verbose_name="Заголовок")),
                ("text", models.TextField(verbose_name="Текст статьи")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")),
                ("user", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name="Автор")),
            ],
            options={"verbose_name": "статья", "verbose_name_plural": "статьи", "ordering": ["-created_at", "id"]},
        ),
        migrations.RunPython(add_initial_articles, migrations.RunPython.noop),
    ]
