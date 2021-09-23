from django.db import models

# Create your models here.

class staffdb(models.Model):
    centername = models.CharField(max_length=200)
    applicantname = models.CharField(max_length=100)
    applicantmobileno = models.IntegerField()
    applicationtype = models.CharField(max_length=100)
    orderpvccard = models.BooleanField()
    totalcharges = models.CharField(max_length=100)
    
class addoperator(models.Model):
    centername = models.CharField(max_length=200, verbose_name='Center Name')
    operatorname = models.CharField(max_length=100, verbose_name='Operator Name')
    operatormob = models.CharField(max_length=20)
    loginid = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    status = models.BooleanField()
    
class addstaff(models.Model):
    name = models.CharField(max_length=30)
    mobileno = models.CharField(max_length=20)
    code = models.CharField(max_length=3)
    loginid = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    status = models.BooleanField()
    
class slotbooking(models.Model):
    centerid = models.IntegerField()
    managed_by = models.CharField(max_length=20)
    appointmentdate = models.DateField()
    bookingdate = models.DateField()
    opening_time = models.TimeField()
    slot_time = models.TimeField()
    booking_status = models.BooleanField()
    
     
    
    

    