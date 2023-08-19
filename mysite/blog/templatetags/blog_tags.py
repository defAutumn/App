from django import template
from django.db.models import Count
from ..models import Post

register = template.Library()


@register.simple_tag # Возвращает значение, которое можно вставить
def total_posts():
    return Post.published.count()


@register.simple_tag
def get_most_commented_posts(count=5):
        # Считает сколько ком-в в кажом посту, сортирует по кол-ву, выбирает count последних
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.inclusion_tag('blog/post/latest_posts.html') # Возвращает словарь
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
