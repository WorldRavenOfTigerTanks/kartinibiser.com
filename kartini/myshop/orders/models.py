from django.db import models
from shop.models import Product


class Order(models.Model):
    CHOICES = [
        ('НП', 'Новая Почта'),
        ('УП', 'Укрпошта'),
    ]
    year_in_school = models.CharField(
        verbose_name='Способ доставки*',
        max_length=2,
        choices=CHOICES,
        default='НП',
    )
    CHOICES2 = [
        ('НП', 'Забрать в отделении'),
        ('УП', 'Доставка курьером'),
    ]
    year_in_school2 = models.CharField(
        verbose_name='',
        max_length=2,
        choices=CHOICES2,
        default='НП',
    )
    first_name = models.CharField(verbose_name='Имя*' , max_length=50, default='')
    last_name = models.CharField(verbose_name='Фамилия*' , max_length=50, default='')
    email = models.EmailField(verbose_name='Email', default='', blank=True)
    address = models.CharField(verbose_name='Адрес' , max_length=250, default='', blank=True)

    postal_code = models.IntegerField(verbose_name='Номер отделения*' , default='')
    postal_code2 = models.CharField(verbose_name='Телефон*' , max_length=20, default='+380')
    city = models.CharField(verbose_name='Город*' , max_length=100, default='')

    city2 = models.TextField(verbose_name='Коментарий' , blank=True , default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity