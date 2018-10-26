from django.contrib import admin

from exercise.models import AppUser,UserActivities
admin.site.register(AppUser)
admin.site.register(UserActivities)
