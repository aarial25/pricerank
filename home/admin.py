from django.contrib import admin
from home.models import Record
from import_export.admin import ExportActionMixin
# Register your models here.

class RecordAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = [field.name for field in Record._meta.get_fields()]
    search_fields = ['cust_group','port',]
    list_filter = ('measure','bussiness_class','meo', 'cust_type', 'mode_delivery', 'rtm_model', 'banding', 'use', 'pack_form')


admin.site.register(Record, RecordAdmin)