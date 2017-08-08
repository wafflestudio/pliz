from rest_framework import serializers
from accounts.models import User
from errands.models import Errand

class UserSerializer(serializers.ModelSerializer):
    errands = serializers.PrimaryKeyRelatedField(many=True, queryset=Errand.objects.all())
      

    class Meta:
      model = User
      fields = ('username','id','email','name','self_introduction','errands')