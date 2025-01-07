from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'phone', 'address')
    search_fields = ('user__username', 'role', 'phone')
    list_filter = ('role',)
