from django.contrib import admin
from django.utils.html import format_html

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ContentInline(admin.StackedInline):
    model = Content
    extra = 1


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_image', 'read_time', 'views', 'comments', 'author', 'datetime', 'category',
                    'published', 'top')
    search_fields = ('title',)
    list_filter = ('category', 'author', 'tags')
    inlines = (ContentInline, CommentInline)

    date_hierarchy = 'datetime'

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 80px; height: 45px;" />', obj.image.url)
        return 'No Image'

    display_image.short_description = 'Image'


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text', 'published', 'article',)
    list_editable = ('published',)
    list_filter = ('article', 'published', 'email')
    search_fields = ('name', 'email')


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'datetime')
    search_fields = ('email',)


class MomentAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_image',)
    search_fields = ('title', 'author',)
    list_filter = ('author',)

    date_hierarchy = 'datetime'

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 80px; height: 45px;" />', obj.image.url)
        return 'No Image'

    display_image.short_description = 'Image'


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'subject', 'created_at', 'connected')
    list_filter = ('connected',)
    search_fields = ('name', 'email', 'subject', 'phone_number')

    date_hierarchy = 'created_at'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Moment, MomentAdmin)
admin.site.register(Contact, ContactAdmin)
