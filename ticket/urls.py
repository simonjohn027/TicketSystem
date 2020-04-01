from django.urls import  path
from .views import TicketListView

app_name = 'ticket'
urlpatterns = [
    path('',TicketListView.as_view(),name = 'index' )
]