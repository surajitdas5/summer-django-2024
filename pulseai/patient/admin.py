from django.contrib import admin
from patient.models import HeartVital, Appointment

# Register your models here.
class HearVitalAdmin(admin.ModelAdmin):
    readonly_fields = ('user',)

class AppontmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'mobile', 'date', 'note', 'status')
    search_fields = ('user', 'mobile')
    list_filter = ('status', 'date' )
    list_editable = ('status',)
    ordering = ('-date',)
    list_per_page = 25


admin.site.register(HeartVital, HearVitalAdmin)
admin.site.register(Appointment, AppontmentAdmin)