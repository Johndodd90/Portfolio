from django.db import models

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class Blog(TimeStampedModel):
    title = models.CharField("Blog Title", max_length=255)
    slug = AutoSlugField("Blog Address", unique=True, always_update=False, populate_from="title")
    content = models.TextField("Content", blank=True)

    def __str__(self):
        return self.title
