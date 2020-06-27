from rest_framework import serializers
from manager.models import UserInfo


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['id', 'name', 'image', 'introduce']


class OneUserInfoSerializer(serializers.ModelSerializer):
    birthday = serializers.DateTimeField(format="%Y-%m-%d", required=False, read_only=True)

    class Meta:
        model = UserInfo
        fields = '__all__'
