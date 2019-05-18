from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserRegisterView, UserProfileView


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile-detail'),
]
