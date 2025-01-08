from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'rank', 'commandery', 'area', 'phone', 'address', 'registration_date')
    search_fields = ('user__username', 'first_name', 'last_name', 'rank', 'phone', 'commandery__name', 'area__name')
    list_filter = ('rank', 'commandery', 'area', 'registration_date')
    ordering = ('user__username',)
