from django.contrib.auth.models import User
from django.conf import settings

# app imports
from .models import FacebookProfile
from .facebook import FacebookAuth

_Facebook = FacebookAuth(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)

class FacebookBackend(object):
    @staticmethod
    def authenticate(token=None, user=None):

        if not user:

            _Facebook._access_token(token)
            profile = _Facebook._user_info()
            user, _ = User.objects.get_or_create(username=profile['id'])
            if _:
                user.set_unusable_password()
                user.email = profile.get('email')
                user.first_name = profile.get('first_name')
                user.last_name = profile.get('last_name')

                user.save()

        return user

    @staticmethod
    def get_user(user_id):

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return

    supports_object_permissions = False
    supports_anonymous_user = False