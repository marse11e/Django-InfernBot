from django.urls import path
from .views import (
    TelegramUserListCreateView,
    TelegramUserDetailView,
    CustomObtainAuthToken,
    NotesListCreateView,
    NotesDetailView,
    CreateUserView,
    UserDetail,
    UserList,
)

urlpatterns = [
    path('api-token-auth/', CustomObtainAuthToken.as_view(), name='api_token_auth'),
    path('register/', CreateUserView.as_view(), name='create_user'),
    path('telegram-users/', TelegramUserListCreateView.as_view(), name='telegramuser-list'),
    path('telegram-users/<int:pk>/', TelegramUserDetailView.as_view(), name='telegramuser-detail'),
    path('telegram-users/<int:user_id>/notes/', NotesListCreateView.as_view(), name='notes-list'),
    path('notes/<int:pk>/', NotesDetailView.as_view(), name='notes-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:id>/', UserDetail.as_view(), name='user-detail'),
]
