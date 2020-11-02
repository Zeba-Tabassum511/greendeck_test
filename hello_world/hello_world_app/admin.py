from django.contrib import admin
from .models import data
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(data)



class dataAdmin(ImportExportModelAdmin):
    pass

class dataAdmin(admin.ModelAdmin):
    list_display = ('id','name','brand_name','regular_price_value','offer_price_value','currency','classification_l1','classification_l2','classification_l3','classification_l4','image_url')


