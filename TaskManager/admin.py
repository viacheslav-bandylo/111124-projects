from django.contrib import admin
from TaskManager.models import (
    Task,
    SubTask,
    Category,
)

# registering all models

# creating an Inline form for model SubTask
class SubTaskInline(admin.StackedInline):
    model = SubTask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('short_title',
                    'description',
                    'status',
                    'deadline',
                    'created_at',)
    search_fields = ('title',
                    'description',
                    'status',
                    'deadline',
                    'created_at',)

    inlines = [SubTaskInline]


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('short_title',
                    'description',
                    'task',
                    'status',
                    'deadline',
                    'created_at')
    search_fields = ('title',
                    'description',
                    'status',
                    'deadline',
                    'created_at')

    def update_status(self, request, queryset):
        queryset.update(status='done')

    update_status.short_description = 'Update status to "Done"'

    actions = [update_status]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']