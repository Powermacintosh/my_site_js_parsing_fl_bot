from django.contrib import admin

# Register your models here.


from .forms import FlForm
from .models import Fl, Tag

import re


# Register your models here.

# admin.site.register(Fl)

@admin.register(Fl)
class FlAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'show', 'price', 'ref_link', 'date_p', 'time_p')
    list_filter = ('date_p',)
    # search_fields = ('link',)
	# prepopulated_fields = {'slug': ('title',)}
	# raw_id_fields = ('author',)
	# date_hierarchy = 'publish'
	# ordering = ('status', 'publish')
    # form = FlForm

admin.site.register(Tag)