from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwars = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create new user with encrypted password and return it"""
        return get_user_model().object.create_user(**validated_data)
