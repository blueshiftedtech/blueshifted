from django.contrib import admin
from web.models import WebsiteEmail

# Register your models here.
class WebsiteEmailAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

admin.site.register(WebsiteEmail, WebsiteEmailAdmin)
