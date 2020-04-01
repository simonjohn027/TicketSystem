from django.db import models
from accounts.models import User

PRIORITY= (
    ('LOW',"LOW"),('MEDIUM',"MEDIUM"),('HIGH',"HIGH")
)
TYPE = (("AVAILABE","AVAILABLE"),("NOT AVAILABLE","NOT AVAILABLE"),("CLOSED","CLOSED"))


class Ticket(models.Model):
    ticket_number = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    type = models.CharField(choices=TYPE, max_length=24)
    priority = models.CharField(choices= PRIORITY,max_length=12)
    creator = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    Assigned = models.CharField(max_length=344)

    def __str__(self):
        return str(self.ticket_number)




class Comments(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete= models.DO_NOTHING)

