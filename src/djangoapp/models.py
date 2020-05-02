from django.db import models
from django.db.models.signals import post_save, pre_save
import random
import string
# Create your models here.


def random_string_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Item(models.Model):
    item_id = models.CharField(default=random_string_generator, max_length=100, primary_key=True)
    model_no = models.CharField(max_length=10, blank=True, null=True)
    make = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def _str_(self):
        return self.item_id


class Price(models.Model):
    # item_id = models.CharField(max_length=100)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE,
                                unique=True, primary_key=True, verbose_name="item")
    cost = models.FloatField()
    sell = models.FloatField()

    def _str_(self):
        return self.Item.item_id

    def gross_margin(self):
        return round(((self.sell-self.cost)/self.sell), 2)
