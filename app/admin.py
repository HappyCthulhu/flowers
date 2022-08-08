from django.contrib import admin
from app.models import User, Flower, Transaction, Feedback

admin.site.register(User)
admin.site.register(Flower)
admin.site.register(Transaction)
admin.site.register(Feedback)


