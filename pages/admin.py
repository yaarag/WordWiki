from django.contrib import admin
from pages.models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    search_fields = ['word']


admin.site.register(Page, PageAdmin)
