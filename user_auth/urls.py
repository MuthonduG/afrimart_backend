from django.urls import path
from .views import CustomTokenObtainPairView, getUsers, getUser, registerUser, deleteUser

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/', getUsers, name='get_users'),
    path('users/<int:pk>/', getUser, name='get_user'),
    path('register/', registerUser, name='register_user'),
    path('users/delete/<int:pk>/', deleteUser, name='delete_user'),
]
