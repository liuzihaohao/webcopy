from django.contrib import admin
from .models import messgaelist,settingslist,filedellist
# Register your models here.
class messgaelistAdmin(admin.ModelAdmin):
	list_display = ['id','code','typetf','file','text','time']
	list_display_links = ['id']
	list_filter = ['typetf','time']
	search_fields = ['code','text','file']
admin.site.register(messgaelist,messgaelistAdmin)

class settingslistAdmin(admin.ModelAdmin):
	list_display = ['id','key','val','oth']
	list_display_links = ['id','key']
	search_fields = ['id','key','val','oth']
admin.site.register(settingslist,settingslistAdmin)

class filedellistAdmin(admin.ModelAdmin):
	list_display = ['id','filedir','time']
	list_display_links = ['id','filedir']
	search_fields = ['id','filedir','time']
	list_filter = ['time']
admin.site.register(filedellist,filedellistAdmin)

admin.site.site_title="copy"
admin.site.site_header="copy"

from django.contrib.admin.models import LogEntry
from django.contrib.sessions.models import Session
from django.contrib.contenttypes.models import ContentType

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['action_time','user','content_type','object_id','object_repr','action_flag','change_message']
admin.site.register(LogEntry,LogEntryAdmin)

class SessionAdmin(admin.ModelAdmin):
	list_display = ['session_key','session_data','expire_date']
admin.site.register(Session,SessionAdmin)

class ContentTypeAdmin(admin.ModelAdmin):
	list_display = ['app_label','model']
admin.site.register(ContentType,ContentTypeAdmin)