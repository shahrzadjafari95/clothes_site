from django.contrib import admin

from clothes.models import Contact, All_Type_Clothes, Category


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    data_hierarchy = 'created_date'
    list_display = ['name', 'email', 'created_date']
    list_filter = ['created_date']
    search_fields = ('name', 'email')
    ordering = ['-created_date']


