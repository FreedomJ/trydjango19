from django.contrib import admin

# Register your models here.
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "timeStamp", "update"]
    list_display_links = ["title"]
    list_filter = ["update", "timeStamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)
