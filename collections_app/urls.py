from . import views
from django.urls import path

urlpatterns = [
    path('', views.customer_view, name='customer_view'),
    path('delete_note/<int:note_id>', views.delete_note, name='delete_note'),
    path('edit_note/<int:note_id>', views.edit_note, name='edit_note'),
]