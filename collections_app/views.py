from django.shortcuts import render
from .models import Customer, CustomerTransaction, CollectorNote, PaymentPlan

def customer_view(request):
    customer = Customer.objects.first()
    transactions = CustomerTransaction.objects.all().order_by('transaction_date')
    notes = CollectorNote.objects.all().order_by('created_at')
    plans = PaymentPlan.objects.all()

    return render(
        request,
        'collections/index.html',
        {
            'customer': customer,
            'transactions': transactions,
            'notes': notes,
            'plans': plans,
        },
    )
