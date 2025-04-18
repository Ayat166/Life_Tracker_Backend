from django.urls import path
from .views import RegisterView, LoginView, UserProfileView, UserListView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("all-usernames/", UserListView.as_view(), name="all-usernames"),
]
