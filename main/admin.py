from django.contrib import admin
from .models import User, Article


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'second_name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'publish', 'status')
    list_display_links = ('id', 'title')