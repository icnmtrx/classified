from django.contrib import admin

# Register your models here.
from .models import Category, Region, ClassifiedAd

class CategoryAdmin(admin.ModelAdmin):
    """
    Categories
    """
    list_display = ('id', 'title', 'slug')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)

admin.site.register(Category, CategoryAdmin)

admin.site.register(Region)

@admin.register(ClassifiedAd)
class ClassifiedAdAdmin(admin.ModelAdmin):
    """
        Classified ads
    """
    list_display = ('id',
                    'author',
                    'region',
                    'category',
                    'header',
                    #'body',
                    'price',
                    'date_posted',
                    'date_updated',
                    'active',
                    'moderation'
                    )
    list_display_links = ('header', )
    list_filter = ('author', 'category', 'price')
    #prepopulated_fields = {'slug': ('author', 'header')}
    search_fields = ('author', 'category', 'header', 'date_posted')
    ordering = ('id',)
    exclude = ('slug',)