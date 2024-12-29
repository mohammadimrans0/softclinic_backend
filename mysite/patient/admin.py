from django.contrib import admin
from . import models
# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','mobile_no', 'image']
    
    def first_name(self,obj):
        return obj.user.first_name # patient er sathe user model er connection ache tai user model er kache giye tar first name ke ber kore anlam
    
    def last_name(self,obj):
        return obj.user.last_name
    
    
admin.site.register(models.Patient, PatientAdmin)