from django.contrib import admin
from project.models import (
    Project,
    Developer,
    Tag,
)

# Register your models here.
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'language')
    search_fields = ('name','description', 'language')

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)



admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Developer, DeveloperAdmin)