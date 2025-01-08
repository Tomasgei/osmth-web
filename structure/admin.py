from django.contrib import admin
from .models import Area, Commandery, Membership

@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Commandery)
class CommanderyAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'komtur', 'member_count')
    search_fields = ('name', 'area__name', 'komtur__username')
    list_filter = ('area',)

@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('user', 'commandery', 'joined_at')
    search_fields = ('user__username', 'commandery__name')
    list_filter = ('commandery',)
