from django.contrib import admin

from about_us.models import Team, Feedback


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'is_active', 'place',)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('created_as', 'assessment', 'feedback',)
