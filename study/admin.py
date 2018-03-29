from django.contrib import admin
from .models import Post ,Agora
from django_summernote.admin import SummernoteModelAdmin

##admin.site.register(Comment)
#admin.site.register(Agora)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']
	list_display_links = ['id','title']
	list_filter = ['author']
	list_editable = ['author']
	fields = ('title', 'author', 'content')

@admin.register(Agora)
class AgoraAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author']
	list_display_links = ['id','title']
	list_filter = ['author']
	list_editable = ['author']
	fields = ('title', 'author', 'content')

# @admin.register(Post)
# class PostAdmin(SummernoteModelAdmin):
# 	pass
