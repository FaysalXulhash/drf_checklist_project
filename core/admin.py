from django.contrib import admin
from .models import CheckList, CheckListItem
# Register your models here.


@admin.register(CheckList)
class CheckListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_deleted', 'is_archived', 'created_at', 'updated_at']


@admin.register(CheckListItem)
class CheckListAdmin(admin.ModelAdmin):
    list_display = ['id', 'checklist', 'is_checked', 'created_at', 'updated_at']
