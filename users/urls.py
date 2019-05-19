from django.urls import path
from users.views import UserLoginView, UserLogoutView, UserRegisterView, UserProfileView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('logout/', UserLogoutView.as_view(), name='user-logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('profile/', UserProfileView.as_view(), name='user-profile-detail'),
]
