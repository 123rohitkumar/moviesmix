from django.contrib import admin
from . models import movie

# Register your models here.
class movieAdmin(admin.ModelAdmin):
    list_display = [
        'rdate','moviename','hero','heroiene','rating'
    ]
admin.site.register(movie,movieAdmin)

