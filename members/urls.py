from django.urls import path
from .views import CreateProfileView, UserRegisterView,ProfileView ,successPassword,UserLogin, PasswordsChangerView, AboutFormView, AboutFormUpdateView, EditProfileView
#from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('edit_profile/<int:pk>', EditProfileView.as_view(), name = 'edit_profile'),
    path('edit_about/<int:pk>', AboutFormUpdateView.as_view(), name = 'edit_about'),
    path('create_profile/', CreateProfileView.as_view(), name = 'create_profile'),
    path('create_about/', AboutFormView.as_view(), name = 'create_about'),
    path('profile/<int:pk>', ProfileView.as_view(), name = 'profile-detail' ),
    path('login/', UserLogin.as_view(), name = 'login'),
    path('password/', PasswordsChangerView.as_view(), name = 'password_changer'),
    path('password_success/', successPassword, name='success_password')

]