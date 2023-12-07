from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.utils import timezone
from django.contrib.auth.models import User

from .models import TelegramUser, Notes
from .serializers import TelegramUserSerializer, NotesSerializer, UserSerializer


class TelegramUserListCreateView(generics.ListCreateAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class TelegramUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TelegramUser.objects.all()
    serializer_class = TelegramUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class NotesListCreateView(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        return Notes.objects.filter(user__user_id=user_id)

    def perform_create(self, serializer):
        user_id = self.kwargs["user_id"]
        user = TelegramUser.objects.get(user_id=user_id)
        serializer.save(user=user)


class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, 
            context={'request': request})
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)
        if created:
            return Response({
                'token': token.key, 
                'user_id': user.pk, 
                'username': user.username, 
                'message': 'Token created'
                })
            
        else:
            token.created = timezone.now()
            token.save()
            return Response({
                'token': token.key, 
                'user_id': user.pk, 
                'username': user.username, 
                'message': 'Token refreshed'
                })


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]
    
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        user = User.objects.get(username=request.data['username']) 
        token, created = Token.objects.get_or_create(user=user) 
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)