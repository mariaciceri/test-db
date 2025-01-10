from django import forms
from .models import CollectorNote

class CollectorNoteForm(forms.ModelForm):
    class Meta:
        model = CollectorNote
        fields = ('note',)