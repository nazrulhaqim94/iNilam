from django.urls import path
from .views import DarjahChoices, KelasChoices, SignupView, GetCSRFToken, LoginView, LogoutView, CheckAuthenticatedView, DeleteAccountView, GetUsersView, RoleChoices

urlpatterns = [
    path('authenticated/', CheckAuthenticatedView.as_view()),
    path('register/', SignupView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('delete/', DeleteAccountView.as_view()),
    path('csrf_cookie/', GetCSRFToken.as_view()),
    path('get_users/', GetUsersView.as_view()),
    path('role/', RoleChoices.as_view(), name='role'),
    path('darjah/', DarjahChoices.as_view(), name='darjah'),
    path('kelas/', KelasChoices.as_view(), name='kelas'),
]
