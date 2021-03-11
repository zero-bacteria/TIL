from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)