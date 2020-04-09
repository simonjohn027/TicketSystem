from django import forms
from .models import Ticket,Comments

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['ticket_number', 'description', 'status', 'priority', 'assigned']

    