from django.contrib import admin

from rango.models import Category, Page
from rango.models import UserProfile


# Customising the Admin Interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
