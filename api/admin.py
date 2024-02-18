from django.contrib import admin
from .models import *

# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "specialization", "contact")
    # list_editable = ('name', 'specialization', 'contact')
    search_fields = ("name", "specialization", "contact")
    list_filter = ("name",)
    list_per_page = 10

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "doctor", "patient", "date", "time", "problem")
    search_fields = ("doctor__name", "patient__name", "problem")
    list_filter = ("doctor__name", "patient__name")
    list_per_page = 10


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient)
admin.site.register(Appointment, AppointmentAdmin)
