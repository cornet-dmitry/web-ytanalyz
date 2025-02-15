from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Поля, отображаемые в списке
    search_fields = ('title', 'content')  # Поля для поиска
    list_filter = ('created_at', 'updated_at')  # Фильтры
