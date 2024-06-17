from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Book, Comment, Tag,Books,Poster

admin.site.register(Book)

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url})" style="max-height: 200px;">')


admin.site.register(Comment)
admin.site.register(Tag)
admin.site.reqister(Books)
admin.site.reqister(Poster)
# Register your models here.
