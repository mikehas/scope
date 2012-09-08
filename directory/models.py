from django.db import models
from datetime import datetime

#NOTES
# null=True - This specifies that a field is NOT NULL
# blank=True - Then required is set to False on input Form, Ok to be blank, True = OK!

# Create your models here.
class Interest(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(blank=True, max_length=1000)

  def __unicode__(self):
    return self.name

class Location(models.Model):
  name = models.CharField(max_length=200)
  interest = models.ForeignKey(Interest,blank=True,default=0)
  description = models.CharField(blank=True,max_length=200,default='')
  note = models.CharField(blank=True,max_length=1500,default='')
  address = models.CharField(blank=True,max_length=200,default='')
  city = models.CharField(blank=True,max_length=200,default='')
  phone = models.CharField(blank=True,max_length=200,default='')
  zipcode = models.CharField(blank=True,max_length=200,default='')
  state = models.CharField(blank=True,max_length=200,default='') 
  region = models.CharField(blank=True,max_length=200,default='') 
  country = models.CharField(blank=True,max_length=200,default='')
  longitude = models.DecimalField(blank=True,decimal_places=10,max_digits=50,default=0)
  latitude = models.DecimalField(blank=True,decimal_places=10,max_digits=50,default=0)
  googleaddress = models.CharField(blank=True,max_length=500,default='')
  mod_date = models.DateField(blank=True,default=datetime.now())

  def __unicode__(self):
    return self.name
    
class Operator(models.Model):
  name = models.CharField(max_length=200, default="")
  link = models.CharField(blank=True,max_length=200, default="")
  notes = models.CharField(blank=True,max_length=500, default="")
  
  def __unicode__(self):
    return self.name
  
class Location_operator(models.Model):
  location = models.ForeignKey(Location)
  operator = models.ForeignKey(Operator)
  
  def __unicode__(self):
    return self.location

class Location_hour(models.Model):
  location = models.ForeignKey(Location)
  day = models.CharField(blank=True,max_length=200)
  hopen = models.CharField(blank=True,max_length=15)
  hclose = models.CharField(blank=True,max_length=15)

  def __unicode__(self):
    return self.location

class Service(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)

  def __unicode__(self):
    return self.name

class Location_service(models.Model):
  location = models.ForeignKey(Location)
  service = models.ForeignKey(Service)

  def __unicode__(self):
    return self.location

class Perspective(models.Model):
  location = models.ForeignKey(Location)
  name = models.CharField(max_length=200)
  longitude = models.DecimalField(decimal_places=10,max_digits=50)
  latitude = models.DecimalField(decimal_places=10,max_digits=50)
  heading = models.DecimalField(decimal_places=10,max_digits=50)
  pitch = models.DecimalField(decimal_places=10,max_digits=50)
  zoom = models.DecimalField(decimal_places=10,max_digits=50) 

  def __unicode__(self):
    return self.name

# Report is the experience of a user at a particular location 
class Report(models.Model):
  title = models.CharField(max_length=200)
  location = models.ForeignKey(Location)
  #user = models.ForeignKey(User)
  datecreated = models.DateField()
  dateofvisit = models.DateField()

  def __unicode__(self):
    return self.title

class Project(models.Model):
  name = models.CharField(max_length=200, default="")
  details = models.TextField(blank=True, max_length=1000)
  link = models.CharField(blank=True,max_length=200, default="")
  notes = models.CharField(blank=True,max_length=500, default="")
  create_date = models.DateField(blank=True, default=datetime.now, )

  def __unicode__(self):
    return self.name
    
class Geocode_cache(models.Model):
  location = models.CharField(max_length=200, default="")
  latitude = models.DecimalField(blank=True, decimal_places=10,max_digits=50)
  longitude = models.DecimalField(blank=True, decimal_places=10,max_digits=50)
  create_date = models.DateField(blank=True, default=datetime.now, )

  def __unicode__(self):
    return self.location
  
  


