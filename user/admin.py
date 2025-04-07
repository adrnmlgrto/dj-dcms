from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from user.models import Profile, User

# Register your models here.
# class UserAdmin(BaseUserAdmin):
#     list_display = [
#         'email',
#         'full_name',
#         'is_active',
#         'is_staff',
#         'is_superuser'
#     ]
#     list_filter = [
#         'is_active',
#         'is_staff',
#         'is_superuser'
#     ]
#     search_fields = [
#         'email',
#         'profile__first_name',
#         'profile__last_name'
#     ]
#     readonly_fields = [
#         'date_joined'
#     ]
#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': [
#                     'email',
#                     'password1',
#                     'password2'
#                 ]
#             }
#         ),
#     )
#     fieldsets = [
#         (
#             'Authentication Details',
#             {
#                 'fields': [
#                     'email',
#                     'password'
#                 ]
#             }
#         ),
#         (
#             'Permissions',
#             {
#                 'fields': [
#                     'is_staff',
#                     'is_active',
#                     'is_superuser',
#                     'groups',
#                     'user_permissions'
#                 ]
#             }
#         )
#     ]
#     ordering = ['date_joined']

#     @admin.display(description='Full Name')
#     def full_name(self, obj: User) -> str:
#         """Returns the full name of the user from profile."""
#         return f'{obj.profile.first_name} {obj.profile.last_name}'

# Register the `User`.
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
