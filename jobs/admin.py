from django.contrib import admin
from models import JobProfile, City, Organization, JobType, JobCategory


class JobAdmin(admin.ModelAdmin):
	list_display = ('title', 'location', 'job_type', 'job_category', 'published', 'created')
	search_fields = ('location__name', 'title')
	list_filter = ('created', 'published')
	ordering = ('-created', )

# Register your models here.
admin.site.register(JobProfile, JobAdmin)
admin.site.register(City)
admin.site.register(Organization)
admin.site.register(JobType)
admin.site.register(JobCategory)
