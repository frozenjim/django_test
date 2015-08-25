from django.contrib import admin

from userprofile.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    fields = ('user','nickname','likes_toblerone')


admin.site.register(UserProfile, UserProfileAdmin)
