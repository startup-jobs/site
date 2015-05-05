from django.contrib import admin
from models import JobProfile, City, Organization, JobType, JobCategory

# Register your models here.
admin.site.register(JobProfile)
admin.site.register(City)
admin.site.register(Organization)
admin.site.register(JobType)
admin.site.register(JobCategory)
