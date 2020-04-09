from django.contrib.auth.decorators import login_required
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render,get_object_or_404,get_list_or_404
from django.views.generic.list import ListView
from .serializer import TicketSerializer
from django.contrib import messages

from ticket.models import Ticket

@login_required
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






@api_view(['GET','POST'])
def ticket_list(request,format = None):

    if request.method == "GET":
        return Response()

@api_view(['GET','POST'])
def ticket_details(request,format = None):
        return Response()

@api_view(['GET','POST'])
def ticket_update(request,format = None):
        return Response()

@api_view(['GET','POST'])
def ticket_create(request,format = None):
        return Response()

@api_view(['GET','POST'])
def comment_create(request,format = None):
        return Response()