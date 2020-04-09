from rest_framework import  serializers
from .models import Ticket,Comments

class TicketSerializer(serializers.ModelSerializer):


    class Meta:
        model = Ticket
        fields = ('ticket_number','date','description','status','priority','creator','assigned')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('timestamp', 'body', 'author')