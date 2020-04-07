from django.urls import  path
from .views import index,ticketDetail

app_name = 'ticket'
urlpatterns = [
    path('',index,name = 'index' ),
    path('<int:ticket_id>/',ticketDetail, name='ticketDetail'),
]