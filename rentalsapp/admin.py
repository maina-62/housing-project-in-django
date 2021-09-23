from django.contrib import admin
from . models import Detail,Houses,Tenants

# Register your models here.

class reg1(admin.ModelAdmin):
    list_display=('name','phone','county','national_id')

class reg2(admin.ModelAdmin):
    list_display=('name','house_type','price','location')

class reg3(admin.ModelAdmin):
    list_display=('first_name','second_name','location','phone','payment_method','amount')
    

admin.site.register(Detail , reg1)
admin.site.register(Houses , reg2)
admin.site.register(Tenants , reg3)
