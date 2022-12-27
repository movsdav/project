from django.urls import path, include
from authApp.views import UserSignUpView, UserLoginView

urlpatterns = [
    path('login/', UserLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('register/', UserSignUpView.as_view(), name='register'),
    path('', include('django.contrib.auth.urls')),
]
