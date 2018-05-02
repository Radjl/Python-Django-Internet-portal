from django.contrib import admin


from import_export import resources,fields
from import_export.widgets import FloatWidget, DateWidget, IntegerWidget, CharWidget

from .models import Ship,Comment
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin
from import_export.fields import Field
from django_summernote.admin import SummernoteModelAdmin




class ShipRes(resources.ModelResource):



    class Meta:
        model = Ship

        widgets = {
            'Pubdate': {'format': '%d.%m.%Y'},
        }

class Shipadmin(ImportExportModelAdmin):
    resource_class = ShipRes



admin.site.register(Ship,Shipadmin)
admin.site.register(Comment)

