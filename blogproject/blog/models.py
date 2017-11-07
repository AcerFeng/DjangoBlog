from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     return 


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    # def __unicode__(self):
    #     return 

class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)

    # 正文
    body = models.TextField()

    # 创建时间和最后一次修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，默认情况下 CharField 要求我们必须存入数据，否则就会报错
    excerpt = models.CharField(max_length=200, blank=True)
    # 分类
    # 一篇文章只能有一个分类，一个分类下可以有多篇文章，所以使用 ForeignKey, 即一对多关联关系
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者，这里 User 是从 django.contrib.auth.models 导入的。
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里我们通过 ForeignKey 把文章和 User 关联了起来。
    # 因为我们规定一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系，和 Category 类似。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    # def __unicode__(self):
    #     return 
