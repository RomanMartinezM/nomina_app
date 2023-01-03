from django.contrib import admin
from .models import Payroll

# Register your models here.
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_date', 'file_link')

admin.site.register(Payroll, PayrollAdmin)