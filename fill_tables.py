import django

django.setup()
from app.models import User, Flower, Transaction, Feedback
from mimesis import Person
from random import choice, randint

person = Person('ru')


def create_users(count):
    for _ in range(count):
        # User.objects.create(name='name', surname='surname', role='SR')
        user = User(name=person.name(), surname=person.surname(), role=choice(['CR', 'SR']))
        user.save()


def create_flowers():
    for user in User.objects.filter(role='SR'):
        flower = Flower(name=choice(['CH', 'TL']),
                        price=randint(100, 300),
                        shade=choice(['RD', 'GR', 'BL', 'YL', 'PR', 'OR', 'WH']),
                        available_quantity=randint(1, 50),
                        seller=user,
                        displayed=(choice([True, False])))
        flower.save()


def create_transactions(count):
    for _ in range(count):
        seller = choice(User.objects.filter(role='SR'))
        flowers = Flower.objects.filter(displayed=True).order_by('?')[0]
        transaction = Transaction(seller=seller,
                                  customer=choice(User.objects.filter(role='CR')),
                                  sold_quantity=randint(1, 50),
                                  flowers=flowers)
        transaction.save()


def create_feedbacks():
    for transaction in Transaction.objects.all():
        feedback = Feedback(seller=transaction.seller,
                            customer=transaction.customer,
                            feedback=choice(['good', 'bad', 'excellent']),
                            transaction=transaction)
        feedback.save()


create_users(10)
create_flowers()
create_transactions(5)
create_feedbacks()
# TODO: сделать READme на git с тем, как запускать
# TODO: проверить запуск этого файлика из python