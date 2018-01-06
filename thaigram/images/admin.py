from django.contrib import admin
from .models import Image


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    
    list_display = (
        'caption',
        'location',
        'created_at',
        'updated_at'
    )

    list_filter = (
        'location',
        'created_at'
    )

    search_fields = (
        'location',
    )

    ordering = (
        'location',
    )


