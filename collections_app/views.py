from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Customer, CustomerTransaction, CollectorNote, PaymentPlan
from .forms import CollectorNoteForm

def customer_view(request):
    customer = Customer.objects.first()
    transactions = (
        CustomerTransaction.objects.all().order_by('transaction_date')
        )
    notes = CollectorNote.objects.all().order_by('created_at')
    plans = PaymentPlan.objects.all()

    if request.method == "POST":
        note_form = CollectorNoteForm(request.POST)
        if note_form.is_valid():
            note = note_form.save(commit=False)
            note.customer = customer
            note.save()
            messages.add_message(
                request, 
                messages.SUCCESS, 
                'Note added successfully.'
            )
        else:
            messages.add_message(
                request, 
                messages.ERROR, 
                'Failed to add note.'
            )
        return redirect('customer_view')

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
