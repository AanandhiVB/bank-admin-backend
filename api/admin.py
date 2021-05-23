from django.contrib import admin

# Register your models here.

from .models import Bank, Branch
 
admin.AdminSite.site_header = "Bank Administration"

class BankAdmin(admin.ModelAdmin):
    list_display=('id', 'name')

class BranchAdmin(admin.ModelAdmin):
    list_display=('id','ifsc','branch','address','city','district','state','bank_id')


 
admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)

