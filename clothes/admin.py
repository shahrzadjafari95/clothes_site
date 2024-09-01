from django.contrib import admin

from clothes.models import Contact, All_Type_Clothes, Category
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter, DropdownFilter
from rangefilter.filters import DateRangeFilter
from django_admin_filters import MultiChoice


# Register your models here.
class GenderFilter(MultiChoice):
    FILTER_LABEL = "By gender"


class StatusFilter(MultiChoice):
    FILTER_LABEL = "By status"


class ContactAdmin(admin.ModelAdmin):
    data_hierarchy = 'created_date'
    list_display = ['name', 'email', 'created_date']
    list_filter = [('created_date', DateRangeFilter)]
    search_fields = ('name', 'email')
    ordering = ['-created_date']


class All_Type_Clothes_Admin(admin.ModelAdmin):
    data_hierarchy = 'created_date'
    list_display = ['gender', 'category', 'price', 'status', 'created_date']
    list_filter = [('status', StatusFilter),
                   ('gender', GenderFilter),
                   ('category', RelatedDropdownFilter),
                   ('created_date', DateRangeFilter)]

    search_fields = ('gender',)
    empty_value_display = '-empty-'
    ordering = ['-created_date']


class Category_Admin(admin.ModelAdmin):
    search_fields = ('name_category',)
    list_display = ['name_category', 'id']


admin.site.register(Contact, ContactAdmin)
admin.site.register(All_Type_Clothes, All_Type_Clothes_Admin)
admin.site.register(Category, Category_Admin)
