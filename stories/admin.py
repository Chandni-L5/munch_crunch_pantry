from django.contrib import admin
from django.urls import reverse

from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'origin_country')
    list_filter = ('is_published', 'created_at', 'origin_country')
    readonly_fields = ('created_at',)

    def preview_link(self, obj):
        if not obj.slug:
            return "Save the story to generate preview link"
        url = reverse('story_preview', args=[obj.slug])
        return f'<a href="{url}" target="_blank">Preview Story</a>'

    preview_link.allow_tags = True
    preview_link.short_description = "Preview Link"
