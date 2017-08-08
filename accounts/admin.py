from django.contrib import admin
from .models import User
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Group
from errands.models import Errand


class TokenInline(admin.StackedInline):
    model = Token

class ErrandInline(admin.StackedInline):
    model = Errand

class UserAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'name','self_introduction')
    inlines = [TokenInline,ErrandInline,]


admin.site.unregister(Group)
admin.site.register(User, UserAdmin)