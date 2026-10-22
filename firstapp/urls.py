from django.urls import path, re_path
from firstapp import views

urlpatterns = [
    path("", views.index, name="home"),
    path("article/<int:article_id>/", views.show_article, name="article"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("form/", views.form_page, name="form"),
    re_path(r"^products/$", views.products),
    re_path(r"^products/(?P<productid>\d+)/?$", views.products),
    re_path(r"^users/(?P<id>\d+)/(?P<name>[^/]+)/?$", views.users),
    re_path(r"^users/$", views.users),
    re_path(r"^students/(?P<id>\d+)/(?P<name>[^/]+)/?$", views.students),
    re_path(r"^students/$", views.students),
    path("login/", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    path("logout/", views.doLogout, name="logout"),
    path("me/", views.me, name="me"),
    path("adaptive/", views.adaptive, name="adaptive"),
]