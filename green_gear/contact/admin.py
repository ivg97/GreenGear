from django.contrib import admin

from contact.models import CommunicationService


@admin.register(CommunicationService)
class CommunicationServiceAdmin(admin.ModelAdmin):
    list_display = ('subject', 'full_name', 'created_at', 'email', 'message',)
    list_display_links = ('subject',)
