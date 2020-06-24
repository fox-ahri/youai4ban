from rest_framework import serializers
from manager.models import User, UserInfo


class UserSerializer(serializers.ModelSerializer):
    password = ''

    class Meta:
        model = User
        fields = '__all__'


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
