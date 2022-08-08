from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    ROLE = [
        ('CR', 'Customer'),
        ('SR', 'Seller'),
    ]

    name = models.CharField(max_length=255, null=False)
    surname = models.CharField(max_length=255, null=False)
    role = models.CharField(max_length=255, choices=ROLE)
    objects = models.Manager()

    def __str__(self):
        return f'{self.name} {self.surname}: {self.role}'

    class Meta:
        db_table = 'users'  # название таблицы
        verbose_name = 'Users'  # название, которое отображается в интерфейсе


class Flower(models.Model):
    id = models.AutoField(primary_key=True)

    SHADES = [
        ('RD', 'Red'),
        ('GR', 'Green'),
        ('BL', 'Blue'),
        ('YL', 'Yellow'),
        ('PR', 'Purple'),
        ('OR', 'Orange'),
        ('WH', 'White'),
    ]

    NAMES = [
        ('CH', 'Chamomile'),
        ('TL', 'Tulip'),
    ]

    name = models.CharField(max_length=255, choices=NAMES, default=None)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='seller_of_flowers', null=False,
                               limit_choices_to={'role': 'SR'}, default=None)
    shade = models.CharField(max_length=255, choices=SHADES, default=None)
    displayed = models.BooleanField(default=False)
    available_quantity = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return f'{self.name}: {self.shade}: {self.seller.surname}'

    class Meta:
        db_table = 'flowers'  # название таблицы
        verbose_name = 'Flowers'  # название, которое отображается в интерфейсе


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='seller', null=False,
                               limit_choices_to={'role': 'SR'}, default=None)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='customer', null=False,
                                 limit_choices_to={'role': 'CR'}, default=None)
    # flowers = models.ManyToManyField(Flower, default=None)
    flowers = models.ForeignKey(Flower, default=None, on_delete=models.CASCADE, related_name='flowers', null=False)
    sold_quantity = models.IntegerField(default=None)
    objects = models.Manager()

    def __str__(self):
        return f'{self.seller.surname} {self.customer.surname}: {self.sold_quantity}'

    class Meta:
        db_table = 'transactions'  # название таблицы
        verbose_name = 'Transactions'  # название, которое отображается в интерфейсе


class Feedback(models.Model):
    id = models.AutoField(primary_key=True)
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='seller_feedback', null=False,
                               limit_choices_to={'role': 'SR'}, default=None)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='customer_feedback', null=False,
                                 limit_choices_to={'role': 'CR'}, default=None)
    feedback = models.TextField(default=None)
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, related_name='transaction_feedback',
                                    null=False, default=None)
    objects = models.Manager()

    def __str__(self):
        return f'{self.seller.name} {self.seller.surname}: {self.customer.name} {self.customer.surname}: {self.feedback}'

    class Meta:
        db_table = 'feedbacks'  # название таблицы
        verbose_name = 'Feedbacks'  # название, которое отображается в интерфейсе