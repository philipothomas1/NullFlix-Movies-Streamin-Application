from django.contrib import admin
from .models import Movie,Review,MovieGenre,SubPlan,SubPlanFeature,SubPlanDiscount,Subscription
from . import models
# Register your models here.

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(MovieGenre)
# admin.site.register(SubPlan)
# admin.site.register(SubPlanFeature)
# admin.site.register(Season)
# admin.site.register(Episode)


# class SeasonInline(admin.TabularInline):
#     model=Season

# class TVSeriesAdmin(admin.ModelAdmin):
#     inlines=[SeasonInline]

# # class EpisodeInline(admin.TabularInline):
# #     model=Episode.through.B

# # class TVSeriesAdmin(admin.ModelAdmin):
# #     inlines=[EpisodeInline]

# admin.site.register(TVSeries,TVSeriesAdmin)

class SubPlanAdmin(admin.ModelAdmin):
    	list_display=('title','subprice','highlight_status','validity_days')
admin.site.register(SubPlan,SubPlanAdmin)

class SubPlanFeatureAdmin(admin.ModelAdmin):
        list_display=('title','subplans')     
        def subplans(self,obj):
            return " | ".join([sub.title for sub in obj.subplan.all()])
admin.site.register(SubPlanFeature,SubPlanFeatureAdmin)


class SubPlanDiscountAdmin(admin.ModelAdmin):
    	list_display=('subplan','total_months','total_discount')
admin.site.register(SubPlanDiscount,SubPlanDiscountAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    	list_display=('user','plan','price','reg_date')
admin.site.register(Subscription,SubscriptionAdmin)



