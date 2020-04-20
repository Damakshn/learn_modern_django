import factory
import factory.fuzzy
from . import models

class UserFactory(factory.django.DjangoModelFactory):
    email = "user@site.com"

    class Meta:
        model = models.User
        django_get_or_create = ("email",)

class ProductFactory(factory.django.DjangoModelFactory):
    price = factory.fuzzy.FuzzyInteger(100, 3000, 2)

    class Meta:
        model = models.Product

class AddressFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Address
