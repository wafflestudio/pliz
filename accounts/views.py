from django.shortcuts import render
from accounts.serializers import UserSerializer
from rest_framework import generics, status
from accounts.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

@api_view(['POST'])
def user_signup(request):
    def is_valid_email(email):
        try:
            validate_email(email)
            return True
        except ValidationError:
            return False

    data = request.data
    username = data.get('username', '')
    password = data.get('password', '')
    password_confirm = data.get('passwordConfirm', '')
    email = data.get('email', '')

    if len(username) < 6:
        return Response(data={'message':'invalid username, must be at least 6 characters long'}, status=status.HTTP_403_FORBIDDEN)

    if password != password_confirm:
        return Response(data={'message':'please confirm input password'}, status=status.HTTP_403_FORBIDDEN)

    if len(password) < 8:
        return Response(data={'message':'password must be at least 8 characters long'}, status=status.HTTP_403_FORBIDDEN)

    if not is_valid_email(email):
        return Response(data={'message':'invalid email'}, status=status.HTTP_403_FORBIDDEN)

    user, created = User.objects.get_or_create(username=username)
    if created:
        user.email=email
        user.set_password(password)
        user.save()
        return Response(data={'message':'user registration successful'}, status=status.HTTP_201_CREATED)
    return Response(data={'message':'duplicated id'}, status=status.HTTP_403_FORBIDDEN)


class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset=User.objects.all()
    serializer_class= UserSerializer


