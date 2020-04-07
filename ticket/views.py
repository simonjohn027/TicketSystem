from django.http import Http404
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic.list import ListView

from ticket.models import Ticket


def index(request):
    ticket = get_list_or_404(Ticket)
    context = {
        'ticket_list':ticket
    }
    return render(request,'ticket/index.html',context)

    
def ticketDetail(request, ticket_id):
    ticket = get_object_or_404(Ticket,pk = ticket_id)
    comments = ticket.comments_set.all()
    ticket_list = Ticket.objects.all()
    context = {
        "ticket": ticket,
        "ticket_list":ticket_list,
         "comment_list":comments
    }
    return render(request, 'ticket/index.html',context)
