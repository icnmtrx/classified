from django.contrib import admin
from .models import Profile


# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    """
        Profiles
    """
    list_display = ('id', 
                    'user',
                    'phone',
                    'first_name',
                    'last_name',
                    'registered_at',
                    'last_updated_at',
                    )
    list_display_links = ('user', )
#    prepopulated_fields = {'slug': ('author', 'header')}
#    search_fields = ('author', 'category', 'header', 'date_posted')
    ordering = ('user',)

admin.site.register(Profile, ProfileAdmin)