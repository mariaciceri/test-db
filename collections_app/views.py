from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import Customer, CustomerTransaction, CollectorNote, PaymentPlan
from .forms import CollectorNoteForm

def customer_view(request):
    customer = Customer.objects.first()
    transactions = (
        CustomerTransaction.objects.all().order_by('-transaction_date')
        )
    notes = CollectorNote.objects.all().order_by('-created_at')
    plans = PaymentPlan.objects.all()

    if request.method == "POST" :
        note_form = CollectorNoteForm(data=request.POST)
        if note_form.is_valid():
            print("testing")
            note = note_form.save(commit=False)
            note.customer = customer
            note.save()
            # if request is ajax, return json response
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "success"})
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({"status": "error", "message": "Failed to add note."})

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

def edit_note(request, note_id):
    if request.method == "POST":
        customer = Customer.objects.first()
        note = get_object_or_404(CollectorNote, pk=note_id)
        noteForm = CollectorNoteForm(request.POST, instance=note)

        if noteForm.is_valid():
            note = noteForm.save(commit=False)
            note.customer = customer
            note.save()

            return JsonResponse({
                "status": "success",
                "updated_note": note.note,
                "note_id": note.id
            })
        
        return JsonResponse({"status": "error", "message": "Failed to update note"})


def delete_note(request, note_id):
    if request.method == "POST":
        note = get_object_or_404(CollectorNote, pk=note_id)
        note.delete()
        return JsonResponse({"status": "success"})

