from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .models import User, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .email_article_form import EmailArticleForm
from .add_article_form import AddArticleForm
from django.core.mail import send_mail
from collections import OrderedDict
from .fusioncharts import FusionCharts
from datetime import datetime


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
    articles_list = Article.objects.filter(status='published')
    paginator = Paginator(articles_list, 3)
    articles_count = paginator.count
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    args = {
        'page': page,
        'articles': articles,
        'articles_count': articles_count
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


def article_share(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    sent = False
    if request.method == 'POST':
        form = EmailArticleForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            article_url = request.build_absolute_uri(article.get_absolute_url())
            subject = '{} ({}) recommends for reading "{}"'.format(cd['name'],
                                                                   cd['email_from'],
                                                                   article.title)

            message = 'Article: "{}".\nLink: {}'.format(article.title, article_url)
            send_mail(subject, message, '1204instagram@gmail.com', [cd['email_to']])
            sent = True
    else:
        form = EmailArticleForm()
    args = {
        'article': article,
        'form': form,
        'sent': sent
    }
    return render(request, 'html/articles/share.html', args)


def add_article(request):
    form = AddArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/articles/')
    args = {
        'form': form
    }
    return render(request, 'html/add_article.html', args)


def article_delete(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug).delete()
    return redirect('/articles/')


def chart(request):
    args = {
        "chart": {
            "caption": "Split of Revenue by Product Categories",
            "subCaption": "Last year",
            "numberPrefix": "$",
            "defaultCenterLabel": "Total revenue: $64.08K",
            "centerLabel": "Revenue from $label: $value",
            "decimals": "0",
            "exportEnabled": "1",
            "theme": "candy",
            "bgColor": "#323232",
            "paletteColors": "#ec407a"
        },
        "data": [
            {
                "label": "Food",
                "value": "28504"
            },
            {
                "label": "Apparels",
                "value": "14633"
            },
            {
                "label": "Electronics",
                "value": "10507"
            },
            {
                "label": "Household",
                "value": "4910"
            }
        ]
    }
    column2d = FusionCharts("column2d", "chart", "800", "600", "chart-container", "json", args)
    output = {
        'column2d': column2d.render()
    }
    return render(request, 'html/chart.html', output)


def test(request):
    return render(request, 'html/test.html')
