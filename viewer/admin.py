from django.contrib import admin
from .models import file_list, movie_name, settings

# Register your models here.
class FileListAdmin(admin.ModelAdmin):
    list_display = ('m_name', 'file_path', 'file_name', 'file_size', 'file_date', 'is_subtitle')
    list_display_links = ['m_name']
    list_per_page = 500

admin.site.register(file_list, FileListAdmin)


class MovieListAdmin(admin.ModelAdmin):
    list_display = ('moviename', 'has_subtitle')
    list_display_links = ['moviename']
    list_per_page = 500


admin.site.register(movie_name, MovieListAdmin)

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('folder_path', 'enabled')

admin.site.register(settings, SettingsAdmin)