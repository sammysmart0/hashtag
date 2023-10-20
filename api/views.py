from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from hashuser.models import CustomUser
from .serializers import Customserializers
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import get_object_or_404


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    serializer = Customserializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = CustomUser.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    user = get_object_or_404(CustomUser, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail":"Not found."}, status=status.HTTP_404_NOT_FOUND)
    return Response({"message":"Login Successful"}, status=status.HTTP_200_OK)

# @api_view(["POST"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([AllowAny])
# def login_view(request):
#     form = AuthenticationForm(data=request.data)

#     if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return Response({"message":"Login successful"}, status=status.HTTP_200_OK)
#     else:
#         return Response({"message":"Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    

    
# class RegistrationView(generics.CreateAPIView):
#     serializer_class = Customserializers

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)