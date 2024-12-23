from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Custom authentication backend to allow users to authenticate using either their email or username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None or password is None:
            return None

        try:
            # Try to get the user by email first
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                # If not an email, try to get the user by username
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # Check the password
        if user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None
