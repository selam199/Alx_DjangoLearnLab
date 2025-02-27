from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.models import Group, Permission
from django.db.models import Q



# Customizing the admin interface for the Book model
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Enable filtering by publication year
    list_filter = ('publication_year',)

    # Enable search functionality for title and author
    search_fields = ('title', 'author')

# Register the Book model with the custom admin configuration
admin.site.register(Book, BookAdmin)

def create_groups_and_permissions():
    # Create Groups
    editors, created = Group.objects.get_or_create(name="Editors")
    viewers, created = Group.objects.get_or_create(name="Viewers")
    admins, created = Group.objects.get_or_create(name="Admins")

    # Assign Permissions
    can_view_permission = Permission.objects.get(codename='can_view')
    can_create_permission = Permission.objects.get(codename='can_create')
    can_edit_permission = Permission.objects.get(codename='can_edit')
    can_delete_permission = Permission.objects.get(codename='can_delete')

    # Assign permissions to groups
    editors.permissions.set([can_view_permission, can_create_permission, can_edit_permission])
    viewers.permissions.set([can_view_permission])
    admins.permissions.set([can_view_permission, can_create_permission, can_edit_permission, can_delete_permission])

# Call this function to set up the groups and permissions
create_groups_and_permissions()


class CustomUserAdmin(UserAdmin):
    """Customize the Django Admin panel for CustomUser"""
    model = CustomUser
    list_display = ('email', 'username', 'date_of_birth', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal Info', {'fields': ('date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'profile_photo', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)