from django.db import models
from django.conf import settings


from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Category(models.Model):
    name = models.CharField(max_length=20)


class Post(TimeStampedModel):
    title = models.CharField("Post Title", max_length=255)
    slug = AutoSlugField("Post Address", unique=True, always_update=False, populate_from="title")
    body = models.TextField("Body", blank=True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    #created_on = models.DateTimeField(auto_now_add=True)
    #last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title


class Comment(TimeStampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )
    body = models.TextField("Body", blank=True)
    #created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
