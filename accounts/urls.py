from django.urls import path
from accounts import views

urlpatterns = [
    path("signup", views.SignupView.as_view(), name="signup"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("signin", views.SigninView.as_view(), name="signin"),
    path("signout", views.signout, name="signout"),
    path("activate/<uidb64>/<token>", views.activate_account, name="activate"),
    path("random", views.random_email_sender, name="random-email"),
]