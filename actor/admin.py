from django.contrib import admin
from .models import Actor

# Register your models here.
# admin.site.register(Actor)

class ActorAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Actor, ActorAdmin)    
