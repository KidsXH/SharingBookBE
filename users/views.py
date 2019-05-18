from rest_framework import permissions
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth

from users.models import User, UserProfile
from users.serializers import UserProfileSerializer


class UserProfileViewSet(ListModelMixin,
                         GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]


class UserLoginView(APIView):
    def post(self, request):
        data = request.data
        user = auth.authenticate(username=data['username'], password=data['password'])

        if user:
            if user.is_disabled:
                return Response({'detail', 'Disabled user'}, status=status.HTTP_400_BAD_REQUEST)
            auth.login(request, user)
            return Response({"detail", "Succeed"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'detail', 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


class UserLogoutView(APIView):
    def get(self, request):
        auth.logout(request)
        return Response({"detail", "Succeed"}, status=status.HTTP_200_OK)


class UserRegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        email = data['email']

        if User.objects.filter(username=username).exists():
            return Response({'detail': 'Username already exist'}, status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=email).exists():
            return Response({'detail': 'Email already exist'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)

        return Response({'detail', 'Succeed'}, status=status.HTTP_201_CREATED)


class UserProfileView(APIView):
    def get(self, request):
        pass

