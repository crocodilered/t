from django.contrib import admin
from .models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_filter = ('created', 'status',)
    search_fields = ('created',)
    list_display = ('id', 'created', 'status',)
    fields = ('id', 'created', 'code', 'status',)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Snippet, SnippetAdmin)
