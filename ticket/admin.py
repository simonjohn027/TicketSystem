from django.contrib import admin

# Register your models here.
from ticket.models import Ticket,Comments

class TicketAdmin(admin.ModelAdmin):
    pass
admin.site.register(Ticket, TicketAdmin)