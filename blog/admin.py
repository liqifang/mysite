from django.contrib import admin
from .models import BlogType, Blog
# Register your models here.


class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ("id",)



class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'blog_type', 'create_time', 'last_updated_time')
    ordering = ("id",)


admin.site.register(BlogType,BlogTypeAdmin)
admin.site.register(Blog,BlogAdmin)