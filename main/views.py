from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from .models import User, Article
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .form import EmailArticleFrom
from django.core.mail import send_mail
from collections import OrderedDict
from .fusioncharts import FusionCharts


def article_share(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    sent = False
    if request.method == 'POST':
        form = EmailArticleFrom(request.POST)
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
        form = EmailArticleFrom()
    args = {
        'article': article,
        'form': form,
        'sent': sent
    }
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


def chart(request):
    # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = "Countries With Most Oil Reserves [2017-18]"
    chartConfig["subCaption"] = "In MMbbl = One Million barrels"
    chartConfig["xAxisName"] = "Country"
    chartConfig["yAxisName"] = "Reserves (MMbbl)"
    chartConfig["numberSuffix"] = "K"
    chartConfig["exportEnabled"] = "1"
    chartConfig["theme"] = "fusion"

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.
    # Insert the data into the `dataSource['data']` list.
    dataSource["data"].append({"label": 'Venezuela', "value": '290'})
    dataSource["data"].append({"label": 'Saudi', "value": '290'})
    dataSource["data"].append({"label": 'Canada', "value": '180'})
    dataSource["data"].append({"label": 'Iran', "value": '140'})
    dataSource["data"].append({"label": 'Russia', "value": '115'})
    dataSource["data"].append({"label": 'Russia', "value": '115'})
    dataSource["data"].append({"label": 'UAE', "value": '100'})
    dataSource["data"].append({"label": 'US', "value": '30'})
    dataSource["data"].append({"label": 'China', "value": '30'})

    # Create an object for the column 2D chart using the FusionCharts class constructor
    # The chart data is passed to the `dataSource` parameter.
    column2D = FusionCharts("spline", "chart", "1000", "600", "chart-container", "json", dataSource)

    args = {
        'output': column2D.render()
    }

    return render(request, 'html/chart.html', args)


def test(request):
    send_mail(
        'One',
        'Two',
        '1204instagram@gmail.com',
        ['nik.makarevskij@yandex.ru'],
        fail_silently=False,
    )
    return HttpResponse('<h1>Sent.</h1>')
