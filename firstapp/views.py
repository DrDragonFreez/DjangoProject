from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import UserForm, LoginForm, RegisterForm, CommentForm
from .models import Article, Comment


def index(request):
    return render(request, "blog/home.html", {"articles": Article.objects.all()})


def show_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                comment = form.save(commit=False)
                comment.article = article
                comment.name = request.user.username
                comment.save()
                return redirect('article', article_id=article.id)
            else:
                return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'blog/article.html', {
        'article': article,
        'comments': article.comment_set.all,
        'form': form,
    })


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")


def form_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        basket = request.POST.get("basket")
        vyb = request.POST.get("vyb")
        email = request.POST.get("email")
        url_text = request.POST.get("url_text")
        file_path = request.POST.get("file_path")
        file = request.FILES.get("file")
        output = ("<h2>Пользователь</h2>"
                  "<h3>Имя-{0}, Возраст-{1}</h3>"
                  "<h4>Положить товар в корзину?  {2}</h4>"
                  "<h4>Вы поедете в Сочи?  {3}</h4>"
                  "<h5>Электронный адрес-{4}</h5>"
                  "<h6>URL-{5}</h6>"
                  "<h7>выбранный файл-{6}</h7>"
                  "<h8>выбранный файл-{7}</h8>").format(
                      name, age, basket, vyb, email, url_text, file_path, file)
        return HttpResponse(output)
    return render(request, "index.html", {"form": UserForm()})


def products(request, productid=1):
    return HttpResponse("<h2>Продукт № {0}</h2>".format(productid))


def users(request, id=1, name="Данил"):
    return HttpResponse("<h2>Пользователь</h2> <h3>id: {0} Имя: {1}</h3>".format(id, name))


def students(request, id=24132, name="Гончаров Данил Сергеевич"):
    return HttpResponse("<h2>Студент</h2> <h3>Номер зачетной книжки: {0}</h3><h4> ФИО: {1}</h4>".format(id, name))


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Неверные данные!')
    return render(request, 'blog/login.html', {'form': form})


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    return render(request, 'blog/registration.html', {'form': form})


def doLogout(request):
    logout(request)
    return redirect('login')


def me(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'blog/me.html', {'user': request.user})

def adaptive(request):
    return render(request, 'blog/adaptive.html')