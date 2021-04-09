from django.contrib import admin

from .models import Order, Polyclinic, Doctor


class OrderAdmin(admin.ModelAdmin):
    list_display = ['polyclinic', 'doctor', 'visit_time', 'full_name', 'policy_number']
    list_filter = ['created', 'updated']


admin.site.register(Order, OrderAdmin)


class PolyclinicAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Polyclinic, PolyclinicAdmin)


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Doctor, DoctorAdmin)
