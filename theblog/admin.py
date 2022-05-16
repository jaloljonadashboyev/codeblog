from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_filter = ('title', 'author','category','post_date')
    list_display = ('title', 'author', 'post_date', 'category','id')
admin.site.register(Category)
admin.site.register(Profile)