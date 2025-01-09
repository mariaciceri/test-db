from django.contrib import admin
from .models import Customer, CustomerTransaction, CollectorNote, PaymentPlan

admin.site.register(Customer)
admin.site.register(CustomerTransaction)
admin.site.register(CollectorNote)
admin.site.register(PaymentPlan)
