# pylint: disable=missing-module-docstring
from django.contrib import admin
from .models import Sequence

class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sequence')
#    list_display_links = ('id', 'title')
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 25

admin.site.register(Sequence, StorageAdmin)
