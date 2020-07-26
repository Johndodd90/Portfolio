from django.template.defaultfilters import slugify

import factory
import factory.fuzzy

from ..models import Blog


class BlogFactory(factory.django.DjangoModelFactory):
    title = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(lambda obj: slugify(obj.title))
    content = factory.Faker(
        'paragraph', nb_sentences=3, variable_nb_sentences=True
    )

    class Meta:
        model = Blog
