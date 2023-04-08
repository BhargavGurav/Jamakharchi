from django.contrib import admin
from .models import Record
# Register your models here.
admin.site.site_header = 'Expense Tracker'

class RecordAdmin(admin.ModelAdmin):
    list_display = ['date', 'amount', 'purpose', 'closing']
    search_fields = ['date', 'purpose']
admin.site.register(Record, RecordAdmin)

