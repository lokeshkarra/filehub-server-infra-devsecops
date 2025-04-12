from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
    TokenRefreshView
)
from .views import UserRegistrationView, UserProfileView, UserProfilePictureView, UserProfilePictureProxyView, ChangePasswordView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    # Authentication Endpoints
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('profile/picture/', UserProfilePictureView.as_view(), name='profile_picture'),
    path('profile/picture/proxy/', UserProfilePictureProxyView.as_view(), name='profile_picture_proxy'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    # Other authentication endpoints
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('reset-password/<int:user_id>/<str:token>/', ResetPasswordView.as_view(), name='reset_password'),
]
