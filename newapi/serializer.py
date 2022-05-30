from .models import users
from rest_framework import serializers
from .models import users

class UserSSerializer(serializers.ModelSerializer):
    class Meta:
        model = users #import posts from model
        # fields = ['username', 'name',] #output values
        fields = '__all__' #output values