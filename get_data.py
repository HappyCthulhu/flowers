import json

import django

django.setup()
from app.models import User, Transaction


def get_users():
    users = User.objects.all()

    return [
        {
            'seller':
                {
                    'name': user.name, 'surname': user.surname
                }
        } for user in users
    ]


def get_filtered_transactions(result):
    for count, elem in enumerate(result):
        transactions = Transaction.objects.filter(seller__name=elem['seller']['name'],
                                                  seller__surname=elem['seller']['surname'])

        result[count]['customers'] = [{'name': transaction.customer.name, 'surname': transaction.customer.surname} for
                                      transaction in transactions]

    return result


def get_summ_of_seller_transactions(result):
    for count, elem in enumerate(result):
        transactions = Transaction.objects.filter(seller__name=elem['seller']['name'],
                                                  seller__surname=elem['seller']['surname'])

        result[count]['purchases_summ'] = sum(
            [transaction.sold_quantity * transaction.flowers.price for transaction in transactions])

    return result


result = get_users()
get_filtered_transactions(result)
get_summ_of_seller_transactions(result)
print(json.dumps(result, indent=4, ensure_ascii=False))
