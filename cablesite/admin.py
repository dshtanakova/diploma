from django.contrib import admin

# Register your models here.
from .models import *

class CableAdmin(admin.ModelAdmin):
    fields = ['cable_mark', 'destination_to', 'destination_from', 'status', 'cross_section', 'lenght']

class PanelAdmin(admin.ModelAdmin):
    fields = ['panel_name', 'location']

class StrandAdmin(admin.ModelAdmin):
    fields = ['id_cable', 'strand_mark', 'resistance_on_earth', 'resistance']

class DeviceAdmin(admin.ModelAdmin):
    fields = ['id_cable', 'id_panel', 'room', 'location', 'device_name']

class ReportAdmin(admin.ModelAdmin):
    fields = ['info']

admin.site.register(Cable, CableAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(Strand, StrandAdmin)
admin.site.register(User)
admin.site.register(Device, DeviceAdmin)
admin.site.register(Report,ReportAdmin)