from django.contrib import admin

from .models import UserPost, UsersRequest, UserComment

# Register your models here.
admin.site.register(UserPost)
admin.site.register(UsersRequest)
admin.site.register(UserComment)
