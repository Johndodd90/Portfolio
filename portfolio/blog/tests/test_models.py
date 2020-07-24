import pytest

from ..models import Blog

# Connects our tests with our database
pytestmark = pytest.mark.django_db


def test___str__():
    blog = Blog.objects.create(
        title="Example Blog Post",
        content="The content of this blog will go here.",
    )
    assert blog.__str__() == "Example Blog Post"
    assert str(blog) == "Example Blog Post"
