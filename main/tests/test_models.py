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

    def test_create_order_works(self):
        p1 = models.Product.objects.create(
            name="The cathedral and the bazaar",
            price=1000,
        )
        p2 = models.Product.objects.create(
            name="Pride and Prejudice", price=200
        )
        user1 = models.User.objects.create_user(
            "user1", "pw432joij"
        )
        billing = models.Address.objects.create(
            user=user1,
            name="John Kimball",
            address1="127 Strudel road",
            city="London",
            country="uk",
        )
        shipping = models.Address.objects.create(
            user=user1,
            name="John Kimball",
            address1="123 Deacon road",
            city="London",
            country="uk",
        )
        basket = models.Basket.objects.create(user=user1)
        models.BasketLine.objects.create(
            basket=basket, product=p1
        )
        models.BasketLine.objects.create(
            basket=basket, product=p2
        )
        with self.assertLogs("main.models", level="INFO") as cm:
            order = basket.create_order(billing, shipping)
        self.assertGreaterEqual(len(cm.output), 1)
        order.refresh_from_db()
        self.assertEquals(order.user, user1)
        self.assertEquals(
            order.billing_address1, "127 Strudel road"
        )
        self.assertEquals(
            order.shipping_address1, "123 Deacon road"
        )
        self.assertEquals(order.lines.all().count(), 2)
        lines = order.lines.all()
        self.assertEquals(lines[0].product, p1)
        self.assertEquals(lines[1].product, p2)
