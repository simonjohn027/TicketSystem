from django.shortcuts import render
from django.views.generic.list import ListView

from ticket.models import Ticket


class TicketListView(ListView):
    model = Ticket
    template_name = 'ticket/index.html'

