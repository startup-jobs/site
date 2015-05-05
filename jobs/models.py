from django.db import models

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = "cities"
	
class Organization(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField(max_length=200)
	city = models.ForeignKey('City')
	
	def __unicode__(self):
		return self.name

class JobType(models.Model):
	type = models.URLField(max_length=200)

	def __unicode__(self):
		return self.type

class JobCategory(models.Model):
	category = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.category

	class Meta:
		verbose_name_plural = "job categories"

class JobProfile(models.Model):
	title = models.CharField(max_length=200)
	location = models.ForeignKey('City')
	post_url = models.URLField(max_length=200)
	job_type = models.ForeignKey('JobType')
	job_category = models.ForeignKey('JobCategory')	

	def __unicode__(self):
		return self.title
