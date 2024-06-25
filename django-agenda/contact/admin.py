from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','name','last_name','email',
    ordering = 'id',
    list_filter = 'created_at',
    search_fields = 'id','name','last_name',
    list_per_page = 10
    list_max_show_all = 100
    list_editable = 'name','last_name',
    list_display_links = 'id',
