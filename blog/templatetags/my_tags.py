# Author:JZW
from django import template
from blog import models
from django.db.models import Count

register = template.Library()

@register.inclusion_tag('left_menu.html')
def get_left_menu(username):
    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog
    print(blog)
    # 我的文章列表
    article_list = models.Article.objects.filter(user=user)

    # 我的文章分类及每个分类下文章数
    # 将我的文章按照我的分类分组，并统计出每个分类下面的文章数
    category_list = models.Category.objects.filter(blog=blog).annotate(c=Count('article')).values('title', 'c')
    tag_list = models.Tag.objects.filter(blog=blog).annotate(c=Count('article')).values('title', 'c')
    # 按日期归档
    archive_list = models.Article.objects.filter(user=user).extra(
        select={"archive_ym": "strftime('%%Y-%%m',create_time)"}
    ).values('archive_ym').annotate(c=Count('nid')).values('archive_ym', 'c')
    return {
        "username": username,
        'category_list':category_list,
        'tag_list':tag_list,
        'archive_list':archive_list
    }