from django.contrib import admin

from user.models import Profile, User

# Register your models here.
admin.site.register(User)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'first_name', 'last_name',
        'birthday', 'gender', 'updated_at'
    ]
    search_fields = [
        'user__email',
        'first_name',
        'last_name'
    ]
    list_filter = ['gender']
    readonly_fields = ['updated_at']
    fieldsets = [
        (
            'Related User',
            {
                'fields': [
                    'user'
                ]
            }
        ),
        (
            'Personal Information',
            {
                'fields': [
                    'avatar',
                    'first_name',
                    'last_name',
                    'birthday',
                    'gender',
                    'updated_at'
                ],
            },
        ),
    ]
