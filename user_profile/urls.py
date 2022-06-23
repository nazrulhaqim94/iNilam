from django.urls import path
from .views import GetUserProfileView, UpdateUserProfileView, GetUserProfileAllView

urlpatterns = [
    path('user/', GetUserProfileView.as_view()),
    path('all_user/', GetUserProfileAllView.as_view()),
    path('update_user/', UpdateUserProfileView.as_view()),
]
