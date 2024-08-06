from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.mail import send_mail
status_list = [
    ('Open','Open'),
    ("In-progress","In-progress"),
    ('Closed','Closed')
]
category_list = [
    ("Hardware","Hardware"),
    ("Software","Software"),
    ("Cloud","Cloud")

]
# Create your models here.
class CreateTicket(models.Model):
    title = models.CharField(max_length=1000,null=False)
    description = models.CharField(max_length=2000,null=False)
    status = models.CharField(max_length=100,choices=status_list,default='Open',null=False)
    category = models.CharField(max_length=100,choices=category_list)
    sub_category = models.CharField(max_length=200,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

  

@receiver(post_save, sender = CreateTicket)
def send_email_on_save(sender, instance, created, **kwargs):
    message = f'''
    Hi Admin,

    New records has created.

    Thanks,
    Admin Team.
'''
    subject = "Records got created"
    send_mail(subject, message, 'sc@datafortune.com',["sachin.deshmukh@datafortune.com",'shivam.dungahu@datafortune.com'])