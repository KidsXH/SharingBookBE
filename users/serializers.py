from rest_framework import serializers
from users.models import UserProfile, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'admin_type')


class UserProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ('id', 'phone_number', 'credit', 'user',
                  'books_read', 'books_reading', 'books_donated',
                  'favorite_books', 'favorite_tags', 'favorite_categories')
