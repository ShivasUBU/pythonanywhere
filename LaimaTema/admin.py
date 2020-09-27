from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile
from OrderManagement.models import TotalSummary, MonthSummary


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class TotalSummaryInline(admin.StackedInline):
    model = TotalSummary
    can_delete = False
    verbose_name_plural = 'TotalSummary'
    fk_name = 'user'


class MonthSummaryInline(admin.StackedInline):
    model = MonthSummary
    can_delete = False
    verbose_name_plural = 'MonthSummary'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, TotalSummaryInline, MonthSummaryInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
