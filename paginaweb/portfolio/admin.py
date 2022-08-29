from django.contrib import admin
from .models import Project
# Create your models here.
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'update')


admin.site.register(Project, ProjectAdmin)