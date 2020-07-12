from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        try:
            
            user = UserModel.objects.get(
                Q(email__icontains = username))
         
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(pk = user_id)
        except UserModel.DoesNotExist:
            return None

        return user 