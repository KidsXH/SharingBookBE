from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.contrib import auth

from users.models import User, UserProfile
from users.serializers import UserProfileSerializer
from utils.permissions import IsAdminUser
from utils.responses import ResponseMsg


class UserProfileViewSet(ListModelMixin,
                         GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminUser, ]


class UserLoginView(APIView):
    def post(self, request):

        if request.user.is_authenticated():
            return ResponseMsg.bad_request('A user has logged in.')

        data = request.data
        username = data.get('username')
        password = data.get('password')

        if username:
            return ResponseMsg.bad_request("'username' field is required.")
        if password:
            return ResponseMsg.bad_request("'password' field is required.")

        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_disabled:
                return ResponseMsg.bad_request('The user is disabled.')
            auth.login(request, user)
            return ResponseMsg.created('Login successfully.')
        else:
            return ResponseMsg.bad_request('Invalid username or password.')


class UserLogoutView(APIView):
    def get(self, request):
        auth.logout(request)
        return ResponseMsg.ok('Logout successfully.')


class UserRegisterView(APIView):
    def post(self, request):
        data = request.data
        username = data['username']
        password = data['password']
        email = data['email']

        if User.objects.filter(username=username).exists():
            return ResponseMsg.bad_request('Username already exist.')
        if User.objects.filter(email=email).exists():
            return ResponseMsg.bad_request('Email already exist.')

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user)

        return ResponseMsg.created('Register Successfully.')


class UserProfileView(APIView):
    def get(self, request):
        pass

