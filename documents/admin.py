from django.contrib import admin

from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    """
    Admin for manage documents
    """
    list_display = ('title',)
    list_display_links = ('title',)
