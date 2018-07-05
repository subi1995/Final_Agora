from django.contrib import admin
from .models import Agora
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Agora)
class AgoraAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']
	list_display_links = ['id','title']
	list_filter = ['author']
	list_editable = ['author']
	fields = ('title', 'author', 'content')
