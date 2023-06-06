from rest_framework_jwt.authentication import BaseJSONWebTokenAuthentication
from rest_framework import exceptions
from accounts.models import CustomUser, Client

class CustomJWTAuthentication(BaseJSONWebTokenAuthentication):
    def get_user_model(self, payload):
        if 'user_type' in payload and payload['user_type'] == 'client':
            return Client
        return CustomUser

    def authenticate_credentials(self, payload):
        user = self.get_user_model(payload)
        try:
            return (user.objects.get(pk=payload['user_id']), None)
        except user.DoesNotExist:
            raise exceptions.AuthenticationFailed('Invalid token.')
