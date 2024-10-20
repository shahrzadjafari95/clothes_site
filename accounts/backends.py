from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Custom authentication backend to allow users to authenticate using either their email or username.
    """

    def authenticate(self, request, username=None, password=None, **kwargs):
