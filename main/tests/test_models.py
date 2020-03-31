from django.test import TestCase
from main import models


class TestModel(TestCase):

    def test_active_manager_works(self):
        models.Product.objects.create(
            name="The cathedral and the bazar",
            price=1000
        )
        models.Product.objects.create(
            name="The Tale of Genji",
            price=3000
        )
        models.Product.objects.create(
            name="The art of programming",
            price=3000,
            active=False
        )
        self.assertEqual(len(models.Product.objects.active()), 2)
