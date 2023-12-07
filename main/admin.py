from django.contrib import admin
from .models import TelegramUser, Notes


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'get_name', 'language_code', 'is_bot', 'created_at')
    search_fields = ['user_id', 'username', 'first_name', 'last_name']
    list_filter = ['is_bot']
    date_hierarchy = 'created_at'
    readonly_fields = ['created_at']

    def get_name(self, obj):
        return obj.get_name()

    get_name.short_description = 'Name'
    get_name.admin_order_field = 'username'


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('user', 'short_text', 'created_at')
    search_fields = ['user__user_id', 'text']
    list_filter = ['user__user_id']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'

    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text

    short_text.short_description = 'Text'


admin.site.site_header = "Infern Bot Admin"
admin.site.site_title = "Infern Bot Admin"
