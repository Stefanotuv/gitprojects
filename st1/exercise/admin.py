from django.contrib import admin

from exercise.models import AppUser,UserActivities, Website, SiteType
admin.site.register(AppUser)
admin.site.register(UserActivities)
admin.site.register(Website)
admin.site.register(SiteType)
