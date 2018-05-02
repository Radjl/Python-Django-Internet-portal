from django.contrib import admin

# Register your models here.


from django.contrib import admin

from import_export import resources,fields
from import_export.widgets import FloatWidget, DateWidget, IntegerWidget, CharWidget

from .models import Inventory
from import_export.admin import ImportExportModelAdmin, ImportExportMixin, ImportMixin, ExportActionModelAdmin, ImportExportActionModelAdmin
from import_export.fields import Field




class InventRes(resources.ModelResource):



    class Meta:
        model = Inventory

        widgets = {
            'Comissioning': {'format': '%d.%m.%Y'},
        }

class InventAdmin(ImportExportModelAdmin):
    resource_class = InventRes



admin.site.register(Inventory,InventAdmin)




