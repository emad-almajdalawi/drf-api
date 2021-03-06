from pyexpat import model
from rest_framework import serializers
from my_snacks_api.models import Snack

class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','title', 'description', 'calories', 'user')
        model = Snack