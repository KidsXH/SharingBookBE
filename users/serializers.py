from rest_framework import serializers
from users.models import UserProfile, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        field = ('url', 'id', 'username', 'email', 'admin_type')


class UserProfileSerialize(serializers.HyperlinkedRelatedField):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        filed = ('url', 'id', 'user', 'phone_number', 'credit', 'avatar',
                 'books_read', 'books_reading', 'books_donated',
                 'favorite_books', 'favorite_tags', 'favorite_categories')
