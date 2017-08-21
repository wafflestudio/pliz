from django.shortcuts import render

from rest_framework import generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.settings import api_settings

from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from accounts.models import User
from errands.models import Errand

from accounts.serializers import UserSerializer
from errands.serializers import ErrandSerializer


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
    email = data.get('email', '')
    name = data.get('name', '')

    if len(username) < 6:
        return Response(data={'message':'invalid username, must be at least 6 characters long'}, status=status.HTTP_403_FORBIDDEN)

    if not is_valid_email(email):
        return Response(data={'message':'invalid email'}, status=status.HTTP_403_FORBIDDEN)

    user, created = User.objects.get_or_create(username=username)
    if created:
        user.email=email
        user.name=name
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


@permission_classes((permissions.IsAuthenticated,))
@api_view(['GET'])
def user_errand_list(request):
    if request.method == 'GET':
        pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
        paginator = pagination_class()
        user = request.user
        queryset=Errand.objects.filter(owner=user)
        page = paginator.paginate_queryset(queryset, request)
        serializer = ErrandSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


@permission_classes((permissions.IsAuthenticated,))
@api_view(['GET'])
def user_profile(request):
    if request.method == 'GET':
        user = request.user
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)


@permission_classes((permissions.IsAuthenticated,))
@api_view(['POST'])
def update_user_introduction(request):
    if request.method == 'POST':
        data = request.data
        user = request.user
        user.self_introduction = data.get('self_introduction', '')
        user.save()
        return Response(data={'message':'user registration successful'})

