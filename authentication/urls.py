from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import AuthUserRegistrationView,AuthUserLoginView, ClerkLoginView, ClerkRegistrationView, StoreAdminRegistrationView,UserListView


urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', AuthUserRegistrationView.as_view(), name='register'),
    path('registerclerk/', ClerkRegistrationView.as_view(), name='register_clerk'),
    path('registerstoreadmin/', StoreAdminRegistrationView.as_view(), name='register_storeadmin'),
    path('login/', AuthUserLoginView.as_view(), name='login'),
    path('loginmerchant/', ClerkLoginView.as_view(), name='login_merchant'),
    path('users/', UserListView.as_view(), name='users'),
]