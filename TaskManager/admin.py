from django.contrib import admin
from TaskManager.models import (
    Task,
    SubTask,
    Category,)

# registering all models

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'description',
                    'status',
                    'deadline',
                    'created_at',)
    search_fields = ('title',
                    'description',
                    'status',
                    'deadline',
                    'created_at',)


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title',
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


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']