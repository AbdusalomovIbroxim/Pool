from django.urls import path
from .views import UserListView, UserDetailView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('list/', UserListView.as_view(), name='user-list'),
    path('detail/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),

]
