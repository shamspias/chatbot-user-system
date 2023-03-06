from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from ausers.models import User, NoneExistNumbers


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            _('Personal info'),
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'phone_number',
                    'subscription_status',
                    'stripe_id',
                )
            },
        ),
        (_('Profile image'), {'fields': ('profile_picture',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    search_fields = ('email', 'stripe_id', 'phone_number')
    list_display = ("email", "first_name", "phone_number", "stripe_id", "subscription_status")


class NoneExistNumberAdmin(admin.ModelAdmin):
    """
    Admin functionality for None Exist Number
    """

    list_display = ("number", "is_user", "text_count")


admin.site.register(NoneExistNumbers, NoneExistNumberAdmin)
# admin.site.register(ConversationHistory)
