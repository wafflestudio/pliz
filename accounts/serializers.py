from rest_framework import serializers
from accounts.models import User
from errands.models import Errand

class UserSerializer(serializers.ModelSerializer):
    errands = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
      model = User
      fields = ('id','email','username', 'errands','name','self_introduction')