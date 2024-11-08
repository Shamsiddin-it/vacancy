from django.contrib import admin
from .models import *


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'duration', 'address', 'salary',)
    search_fields = ('name', 'category__name', 'duration', 'address', 'salary',)
    list_filter = ('name', 'category', 'duration', 'address', 'salary',)
     