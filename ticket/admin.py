from django.contrib import admin
from .models import CreateTicket

# Register your models here.

class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'sub_category']

admin.site.register(CreateTicket,TicketAdmin)


