from django.db import models
from django.utils import timezone
from django.urls import reverse
from djangotest.utils import unique_slug_generator
from django.db.models.signals import pre_save


class User(models.Model):
    first_name = models.CharField(max_length=200, null=True)
    second_name = models.CharField(max_length=200, null=True)


class Article(models.Model):
    status = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=200, null=False, default='Nikita Biryukov')
    body = models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. A culpa et explicabo '
                                    'natus odit quod repellendus saepe. Ab autem corporis deleniti dolore ducimus '
                                    'expedita, impedit, labore recusandae rerum saepe veniam?</span><span>Amet dicta '
                                    'distinctio earum esse est iure maiores neque nesciunt nulla omnis optio quaerat '
                                    'quis, rerum, sapiente, similique temporibus velit voluptate voluptatem. '
                                    'Consectetur consequuntur corporis natus nulla qui quos, ullam!')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=status, default='Draft')

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.slug])


class Meta:
    ordering = ('-publish',)


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(slug_generator, sender=Article)


def __str__(self):
    return self.title

