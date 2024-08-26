from django.contrib import admin
from blog.models import Post, Category
from rangefilter.filters import DateRangeFilter
from django_admin_filters import MultiChoice


# Register your models here.

class StatusFilter(MultiChoice):
    FILTER_LABEL = "By status"


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_filter = ('status', 'published_date', 'category')
    list_display = ('title', 'id', 'status', 'author', 'counted_view', 'published_date', 'created_date')
    list_filter = (('status', StatusFilter),
                   ('published_date', DateRangeFilter),
    search_fields = ['title', 'content', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

