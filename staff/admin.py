from django.contrib import admin
from .models import staffdb, addoperator, addstaff, slotbooking
# Register your models here.

@admin.register(staffdb)
class staffdbAdmin(admin.ModelAdmin):
    list_display=['id','applicantname', 'centername','applicantmobileno','applicationtype','totalcharges','orderpvccard']
    list_display_links=['applicantname']
    
@admin.register(addoperator)
class addoperatorAdmin(admin.ModelAdmin):
    list_display=['id','centername','operatorname','operatormob','loginid','password']
    list_display_links=['centername']
    
@admin.register(addstaff)
class addstaffAdmin(admin.ModelAdmin):
    list_display=['id','name','mobileno','code','loginid','password','status']
    list_display_links=['name']
    
@admin.register(slotbooking)
class slotbookingAdmin(admin.ModelAdmin):
    list_display= ['id','centerid','managed_by','appointmentdate','bookingdate','opening_time','slot_time','booking_status']
    list_display_links=['managed_by']
    

    



    
