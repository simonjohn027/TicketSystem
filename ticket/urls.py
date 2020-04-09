from django.urls import  path,reverse_lazy
from django.views.generic import RedirectView

from .views import index,ticketDetail

app_name = 'ticket'
urlpatterns = [
    path('',index,name = 'index' ),
    path('<int:ticket_id>/',ticketDetail, name='ticketDetail'),
    path('admin', RedirectView.as_view(url=reverse_lazy('admin:index')),name='admin'),
]