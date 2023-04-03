from import_export import resources
from ausers.models import User


class UserResource(resources.ModelResource):
    """
    User resource.
    """

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'subscription_status',
            'stripe_id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'date_joined',
        )
