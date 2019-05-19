from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from django.contrib import auth

from users.models import User, UserProfile
from users.serializers import UserProfileSerializer
from utils.permissions import IsAdminRole
from utils.responses import ResponseMsg


class UserProfileViewSet(ListModelMixin,
                         GenericViewSet):
    """
    This is user-profiles list view, which lists all user profiles.
    Only admin user has permission.
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAdminRole, ]


class UserLoginView(APIView):
    """
    This is user-login API view.
    Receive username and password trying to log in.
    """
    def post(self, request):
        # If there is a user has logged in, return error message.
        if request.user.is_authenticated():
            return ResponseMsg.bad_request('A user has logged in.')

        data = request.data
        username = data.get('username')
        password = data.get('password')

        # If username or password was missed in request, return error message.
        if username is None:
            return ResponseMsg.bad_request("'username' field is required.")
        if password is None:
            return ResponseMsg.bad_request("'password' field is required.")

        # Try to log in and get the user instance.
        # If username is not found or password is invalid, the value of user will be None.
        user = auth.authenticate(username=username, password=password)

        if user:
            if user.is_disabled:
                return ResponseMsg.bad_request('The user is disabled.')
            auth.login(request, user)
            return ResponseMsg.created('Login successfully.')
        else:
            return ResponseMsg.bad_request('Invalid username or password.')


class UserLogoutView(APIView):
    """
    This is user-logout API view.
    After log out, request.user will be set to an instance of AnonymousUser.
    """
    def get(self, request):
        auth.logout(request)
        return ResponseMsg.ok('Logout successfully.')


class UserRegisterView(APIView):
    """
    This is user-register API view.
    You could use this API to create a new user.
    Username, password, email address are required.
    Username and email address should be unique.
    """
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        # Check if any fields are missed
        if username is None:
            return ResponseMsg.bad_request("'username' field is required.")
        if password is None:
            return ResponseMsg.bad_request("'password' field is required.")
        if email is None:
            return ResponseMsg.bad_request("'email' field is required.")

        # Check if username and email address are unique.
        if User.objects.filter(username=username).exists():
            return ResponseMsg.bad_request('Username already exist.')
        if User.objects.filter(email=email).exists():
            return ResponseMsg.bad_request('Email already exist.')

        # Create user and set password, user's admin type is 'Regular User' by default.
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        # Create user profile related to the user.
        UserProfile.objects.create(user=user)

        return ResponseMsg.created('Register Successfully.')


class UserProfileView(APIView):
    """
    This is user-profile-detail API view.
    Users can only see their own profile.
    Of course, login is required.
    """
    def get(self, request):
        # If user has not logged in, return error message.
        if not request.user.is_authenticated:
            return ResponseMsg.forbidden('Please log in first.')

        # Get user profile from database related to currently logged in user.
        user_profile = UserProfile.objects.get(user=request.user)
        serializer = UserProfileSerializer(user_profile)

        return ResponseMsg.ok(data=serializer.data)
