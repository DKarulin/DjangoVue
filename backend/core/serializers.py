from rest_framework.serializers import ModelSerializer

from core.models import Car
from core.models import Users


class CarSerializers(ModelSerializer):
     class Meta:
         model = Car
         fields = "__all__"

class UsersSerializers(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
