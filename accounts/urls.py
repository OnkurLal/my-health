from django.urls import path
from accounts.views import user_login, user_signup, user_logout

urlpatterns = [
    path("login/", user_login, name="user_login"),
    path("signup/", user_signup, name="user_signup"),
    path("logout/", user_logout, name="user_logout"),
]
