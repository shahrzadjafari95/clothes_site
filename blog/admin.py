from django.contrib import admin
from blog.models import Post, Category, Comment, Newsletter
from rangefilter.filters import DateRangeFilter
from django_admin_filters import MultiChoice
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class StatusFilter(MultiChoice):
    FILTER_LABEL = "By status"


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'id', 'status', 'get_category', 'author', 'login_required', 'counted_view', 'published_date')
    list_filter = (('status', StatusFilter),
                   ('published_date', DateRangeFilter),
                   ('category', RelatedDropdownFilter))
    search_fields = ['title', 'content', 'category']
    summernote_fields = ('content',)

    # To display many-to-many fields in the Django Admin list view, we need to define a custom method in the model admin
    # class and use it in the list_display attribute.
    def get_category(self, obj):
        return ', '.join([category.name for category in obj.category.all()])

    get_category.short_description = 'Category'


class CategoryAdmin(admin.ModelAdmin):
    ordering = ['name']
    list_display = ('name', 'id',)
    search_fields = ['name']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'approved', 'created_date')
    list_filter = ['approved']
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    search_fields = ['email']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Newsletter)
