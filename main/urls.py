from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home),
    path('add_user/', views.add_user, name='add_user'),
    path('add_user_form/', views.add_user_form, name='add_user_form'),
    path('users/', views.users),
    path('articles/', views.article_list, name='article_list'),
    path('articles/<slug:slug_text>', views.article_detail, name='article_detail'),
    path('add_article/', views.add_article),
    path('<article_slug>/share/', views.article_share, name='article_share'),
    path('<article_slug>/delete/', views.article_delete, name='article_delete'),
    path('chart/', views.chart, name='chart'),
    path('test/', views.test, name='test'),

]
