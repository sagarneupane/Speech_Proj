from django.urls import path
from accounts import views

urlpatterns = [
    path("signup", views.SignupView.as_view(), name="signup"),
    path("profile", views.ProfileView.as_view(), name="profile"),
    path("signin", views.SigninView.as_view(), name="signin"),
    path("signout", views.signout, name="signout"),
    path("activate/<uidb64>/<token>", views.activate_account, name="activate"),

    path("password_reset", views.PasswordResetView.as_view(), name="password_reset"),

    path(
        "password_reset/done/",
        views.PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),

    path("random", views.random_email_sender, name="random-email"),
    path("dummy", views.dummy_response, name="dummy-response"),
]