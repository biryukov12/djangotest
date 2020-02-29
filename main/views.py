from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .models import User, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import EmailArticleFrom
from django.core.mail import send_mail


def article_share(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    sent = False
    if request.method == 'POST':
        form = EmailArticleFrom(request.POST)
        print('form if: ', form)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            article_url = request.build_absolute_uri(article.get_absolute_url())
            subject = '{} ({}) recommends for reading "{}"'.format(cd['name'],
                                                                   cd['email_from'],
                                                                   article.title)
            print(subject)

            message = 'Article: "{}".\nLink: {}'.format(article.title, article_url)
            print(message)
            send_mail(subject, message, '1204instagram@gmail.com', [cd['email_to']])
            sent = True
    else:
        form = EmailArticleFrom()
        print('form else: ', form)
    args = {
        'article': article,
        'form': form,
        'sent': sent
    }
    print(args)
    return render(request, 'html/articles/share.html', args)


def custom_404(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request, 'html/404.html', data)


def home(request):
    return render(request, 'html/index.html')


def add_user(request):
    return render(request, 'html/add_user.html')


def add_user_form(request):
    first_name = request.POST['first_name']
    second_name = request.POST['second_name']
    user = User(first_name=first_name, second_name=second_name)
    user.save()
    return redirect('/users/')


def users(request):
    user = User.objects.all()
    args = {'user': user}
    return render(request, 'html/users.html', args)


def article_list(request):
    articles_list = Article.objects.all()
    paginator = Paginator(articles_list, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    args = {
        'page': page,
        'articles': articles
    }

    return render(request, 'html/articles/list.html', args)


def article_detail(request, slug_text):
    a = Article.objects.filter(slug=slug_text)
    arg = "<h1>Article not found. <a href='/articles/'>Go to article list &raquo;</a></h1>"
    if a.exists():
        a = a.first()
    else:
        return HttpResponse(arg)
    articles = Article.objects.all()

    args = {
        'article': a,
        'articles': articles
    }

    return render(request, 'html/articles/detail.html', args)


def add_article(request):
    args = None
    return render(request, 'html/add_article.html', args)


def test(request):
    send_mail(
        'One',
        'Two',
        '1204instagram@gmail.com',
        ['nik.makarevskij@yandex.ru'],
        fail_silently=False,
    )
    return HttpResponse('<h1>Sent.</h1>')
