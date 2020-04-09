from django.contrib import admin
from .models import Ticket, Comments
from django.utils.translation import  ugettext_lazy



admin.site.site_title = ugettext_lazy('Glasgow Caledonian Audio Visual Service ')
admin.site.site_header = ugettext_lazy('Glasgow Caledonian Audio Visual Service ')
admin.site.index_title = ugettext_lazy('GCUAVS')

class CommentInline(admin.TabularInline):
    model = Comments
    extra = 1

class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number','ticket_title','date','status','priority','creator','assigned']
    fieldsets = [
        ('Details',               {'fields': ['ticket_title','description']}),
        ('Ticket Status', {'fields': ['status','priority']}),
        (None, {'fields':['creator','assigned']}),
    ]
    inlines = [CommentInline]

admin.site.register(Ticket, TicketAdmin)