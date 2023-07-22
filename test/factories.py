import factory
import pytest

from faker import Faker
from pytest_factoryboy import register

fake = Faker()

from inventory import models


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        """
        Define a model that we're gonna use
        """
        model = models.Category

    # lexify позволит подставлять символы вместо '?'
    name = fake.lexify(text="cat_name_????")
    slug = fake.lexify(text="cat_slug_????")
    # is_active = fake.lexify()  # factory by default set for bool type - true


register(CategoryFactory)
