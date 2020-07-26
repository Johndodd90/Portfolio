import pytest

from .factories import BlogFactory

from ..models import Blog

# Connects our tests with our database
pytestmark = pytest.mark.django_db


def test___str__():
    blog = BlogFactory()
    assert blog.__str__() == blog.title
    assert str(blog) == blog.title
