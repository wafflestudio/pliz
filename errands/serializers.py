from rest_framework import serializers
from django.contrib.auth.models import User
from errands.models import Errand


class ErrandSerializer(serializers.ModelSerializer):
    owner_name = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Errand
        fields = ('id', 'owner_name', 'title','text','extraCost','reward','category',)
