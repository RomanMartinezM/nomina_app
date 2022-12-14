from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, Roles
from .serializers import UserSerializer, CustomUserSerializer, RegisterSerializer, UserSerializerUpdate, RoleSerializer
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR, LOGIN_CREDENTIALS_ERROR

from django.core.mail import send_mail
from django.conf import settings

import secrets
import string


# Create your views here.
class LoginView(GenericAPIView):
    def get(self, request):
        data_response = {"msg": "Método GET no permitido"}
        return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
        email = request.data.get("email", None)
        code_employee = request.data.get("code_employee", None)
        password = request.data.get("password", None)

        if email is None and code_employee is not None:
            if code_employee is None or password is None:
                return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
            else: 
                try:
                    user = authenticate(code_employee = code_employee, password = password)
                    if user is not None and user.status == True:#user.is_active:
                        token = Token.objects.get_or_create(user=user)
                        if token:
                            return Response( {
                                "token": token[0].key,
                                "user": CustomUserSerializer(user, context = self.get_serializer_context()).data,
                                "message": LOGIN_OK
                            }, status=status.HTTP_200_OK)
                        token.delete()
                        token = Token.objects.create(user=user)
                        return Response( {
                            "token": token[0].key,
                            "user": CustomUserSerializer(user, context = self.get_serializer_context()).data,
                            "message": LOGIN_OK
                        }, status=status.HTTP_200_OK)
        
                    else:
                        return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)
                except:
                        return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)

        elif code_employee is None and email is not None:
            if email is None or password is None:
                return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    user = CustomUser.objects.get(email=email)
                    user = authenticate(code_employee = user.code_employee, password = password)
                    if user is not None and user.status == True:#user.is_active:
                        token = Token.objects.get_or_create(user=user)
                        if token:
                            return Response( {
                                "token": token[0].key,
                                "user": CustomUserSerializer(user, context = self.get_serializer_context()).data,
                                "message": LOGIN_OK
                            }, status=status.HTTP_200_OK)
                        token.delete()
                        token = Token.objects.create(user=user)
                        return Response( {
                            "token": token[0].key,
                            "user": CustomUserSerializer(user, context = self.get_serializer_context()).data,
                            "message": LOGIN_OK
                        }, status=status.HTTP_200_OK)
        
                    else:
                        return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)
                except: 
                        return Response(LOGIN_CREDENTIALS_ERROR, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST) 


@permission_classes([IsAuthenticated])
class LogoutView(GenericAPIView):
    def post(self, request):
        try:
            token_request = request.headers.get("token", None)
            token = Token.objects.get(key=token_request)
            if token: 
                user = CustomUser.objects.filter(auth_token=token).first()
                user.auth_token.delete()
                logout(request)
                return Response({"msg": "Sesion finalizada"},status=status.HTTP_200_OK)
            return Response({"error":"El usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)   
        except:
            return Response({"error":"El usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)   


@permission_classes([IsAuthenticated])
class SignUpView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        token_request = request.headers.get("token", None)
        if token_request is not None:
            # token = Token.objects.get(key=token_request)
            token = Token.objects.filter(key=token_request).first()
            if token:
                log_user = CustomUser.objects.filter(auth_token=token).first()
                if log_user.rol.id == 1:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)
                    user = serializer.save()
                    return Response(
                        {
                            "user": UserSerializer(user, context = self.get_serializer_context()).data,
                            "message": SIGNUP_OK
                        },
                    )
                return Response({"error":"Solo el usuario administrador puede acceder"}, status=status.HTTP_400_BAD_REQUEST) 
            return Response({"error":"Token inexistente"}, status=status.HTTP_400_BAD_REQUEST)   
        return Response({"error":"Token no encontrado"}, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def disable_user(request, user_id):
    token_request = request.headers.get("token", None)
    if token_request is not None:
        # token = Token.objects.get(key=token_request)
        token = Token.objects.filter(key=token_request).first()
        if token:
            log_user = CustomUser.objects.filter(auth_token=token).first()
            if log_user.rol.id == 1:
                try:
                    user = CustomUser.objects.get(id=user_id)
                    user.status = False
                    UserSerializer(user, many=False)
                    user.save()
                    data = {
                        "message": "Usuario deshabilitado exitosamente",
                    }
                    return Response(data, status = 200)
                except:
                    return Response({"error": "No existe ningun usuario con ese ID"}, status = 404)
            return Response({"error":"Solo el usuario administrador puede acceder"}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({"error":"Token inexistente"}, status=status.HTTP_400_BAD_REQUEST)   
    return Response({"error":"Token no encontrado"}, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_user(request, user_id):
    token_request = request.headers.get("token", None)
    if token_request is not None:
        # token = Token.objects.get(key=token_request)
        token = Token.objects.filter(key=token_request).first()
        if token:
            log_user = CustomUser.objects.filter(auth_token=token).first()
            if log_user.rol.id == 1:
                try:
                    user = CustomUser.objects.get(id=user_id)
                    serializer = UserSerializerUpdate(user, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data)
                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                except CustomUser.DoesNotExist:
                    return Response({"error": "No existe ningún usuario con ese ID"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"error":"Solo el usuario administrador puede acceder"}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({"error":"Token inexistente"}, status=status.HTTP_400_BAD_REQUEST)   
    return Response({"error":"Token no encontrado"}, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_users(request):
    token_request = request.headers.get("token", None)
    if token_request is not None:
        # token = Token.objects.get(key=token_request)
        token = Token.objects.filter(key=token_request).first()
        if token:
            log_user = CustomUser.objects.filter(auth_token=token).first()
            if log_user.rol.id == 1:
                users = CustomUser.objects.all()
                serializer = CustomUserSerializer(users, many=True)
                return Response(serializer.data)

            return Response({"error":"Solo el usuario administrador puede acceder"}, status=status.HTTP_400_BAD_REQUEST) 
        return Response({"error":"Token inexistente"}, status=status.HTTP_400_BAD_REQUEST)   
    return Response({"error":"Token no encontrado"}, status=status.HTTP_400_BAD_REQUEST)  


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def change_password(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        current_password = request.data.get("current_password", None)
        new_password = request.data.get("new_password", None)
        confirm_password = request.data.get("confirm_password", None)

        if current_password is None or new_password is None or confirm_password is None:
            return Response({"error": "Todos los datos son obligatorios"}, status.HTTP_400_BAD_REQUEST)

        current_password_is_correct=check_password(current_password, user.password)
        if current_password_is_correct:
            if new_password == confirm_password:
                user.password = make_password(new_password)
                user.save()
                serializer = UserSerializer(user, many=False)
                return Response({
                    "user": serializer.data,
                    "msg": "El password ha sido cambiado exitosamente"
                })
            return Response({"error": "Las contraseñas no coinciden"}, status.HTTP_400_BAD_REQUEST)

        return Response({
                "current_password": current_password,
                "user.password": user.password,
                "error": "La contraseña actual es incorrecta"
                }, status.HTTP_400_BAD_REQUEST)
    except: 
        return Response({"error": "No existe un usuario con ese id"}, status.HTTP_400_BAD_REQUEST)


@api_view(['POST']) 
def recovery_password(request):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = '._-$#%?¿¡!' #string.punctuation
    alphabet = lowercase_letters + uppercase_letters + digits + special_chars
    pwd_length = 13

    while True:
        new_pwd = ''
        for i in range(pwd_length):
            new_pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in new_pwd) and sum(char in digits for char in new_pwd)>=1 and 
            any(char in lowercase_letters for char in new_pwd) and any(char in uppercase_letters for char in new_pwd)):
                break

    email = request.data.get("email", None)
    if email is None or email == '': 
        return Response({"error": "Por favor, introduzca su email"}, status.HTTP_400_BAD_REQUEST)
    try:
        user = CustomUser.objects.get(email=email)
        message = "Se le ha enviado un correo electrónico en respuesta a su solicitud de recuperación de contraseña. Debería recibirlo en un lapso de tiempo corto. Asegurese de revisar su carpeta de spam."
        message_email = f"Recibimos su solicitud para recuperar su contraseña.\nSu nueva contraseña es: {new_pwd}\nAhora puede iniciar sesión usando su nueva contraseña."
        try:    
            send_mail( 
                'Recuperación de contraseña',# 'Subject here',
                message_email,# 'Here is the message.',
                settings.EMAIL_HOST_USER,# 'from@example.com',
                [email],# ['to@example.com'],
                fail_silently=False,
            )
            user.password = make_password(new_pwd)
            user.save()
            serializer = UserSerializer(user, many=False)
            return Response({
                "user": serializer.data,
                "msg": message
            })
        except: 
            return Response({"error":"El email no se envió correctamente, por favor, vuelva a ingresar su dirección de correo electrónico"}, status=400)

    except:
        return Response({"error":"El email no corresponde a ningún usuario registrado"}, status=400)


@api_view(['POST'])
def create_role(request):
    role_name = request.data.get("role_name", None)
    role = Roles.objects.create(
        rol_name = role_name
    )
    serializer = RoleSerializer(role, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_roles(request):
    roles = Roles.objects.all()
    serializer = RoleSerializer(roles, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def enable_user(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        user.status = True
        serializer = CustomUserSerializer(user, many=False)
        user.save()
        data = {
            "user": serializer.data,
            "message": "Usuario habilitado exitosamente",
        }
        return Response(data, status = 200)
    except:
        return Response({"error": "No existe ningun usuario con ese ID"}, status = 404)