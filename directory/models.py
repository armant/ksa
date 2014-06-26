from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class KSA(models.Model):
	user = models.OneToOneField(User)
	ksa_name = models.CharField(max_length=200, blank=True)
	president_name = models.CharField(max_length=200, blank=True)
	president_contact = models.CharField(max_length=200, blank=True)
	president_photo = models.ImageField(upload_to='president_photos/', blank=True)
	key_people = models.TextField(blank=True)
	housing_info = models.TextField(blank=True)
	facebook_group = models.URLField(max_length=999, blank=True)
	note = models.TextField(blank=True)
	
	def __unicode__(self):
		return self.ksa_name
"""
class Album(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.FileField(upload_to="images/")
    albums = models.ManyToManyField(Album, blank=True)
"""