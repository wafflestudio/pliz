from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    errands = serializers.HyperlinkedRelatedField(many=True, view_name='bills-detail', read_only=True)

    class Meta:
      model = User
      fields = ('url','id','email','username', 'errands','name','self_introduction')