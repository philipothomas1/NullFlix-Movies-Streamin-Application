from django.contrib import admin

from .models import TVSeries,Season,Episode

# Register your models here.

class TvSeriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tv_series_name",)}
    
class SeasonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("season_number",)}
# Register your models here.
admin.site.register(TVSeries,TvSeriesAdmin)
admin.site.register(Season,SeasonAdmin)
admin.site.register(Episode)
