from django.contrib import admin

from clothes.models import Contact, All_Type_Clothes, Category


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    data_hierarchy = 'created_date'
    list_display = ['name', 'email', 'created_date']
    list_filter = ['created_date']
    search_fields = ('name', 'email')
    ordering = ['-created_date']


class All_Type_Clothes_Admin(admin.ModelAdmin):
    data_hierarchy = 'created_date'
    list_display = ['gender', 'category', 'price', 'status', 'created_date']
    list_filter = ['created_date', 'status', 'category', 'gender']
    search_fields = ('gender',)
    empty_value_display = '-empty-'
    ordering = ['-created_date']


class Category_Admin(admin.ModelAdmin):
    search_fields = ('category',)
    list_filter = ['category']


admin.site.register(Contact, ContactAdmin)
admin.site.register(All_Type_Clothes, All_Type_Clothes_Admin)
admin.site.register(Category, Category_Admin)
