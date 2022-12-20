from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password
from rest_framework import status
from rest_framework.response import Response
<<<<<<< HEAD
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .serializers import UserSerializer, UserSerializerWithToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR 
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

# Create your views here.
"""class LoginView(APIView):
=======
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, CustomUserSerializer, RegisterSerializer, UserSerializerUpdate
from .messages.responses_ok import LOGIN_OK, SIGNUP_OK
from .messages.responses_error import LOGIN_CREDENTIALS_REQUIRED_ERROR, LOGIN_CREDENTIALS_ERROR

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
class LoginView(GenericAPIView):
>>>>>>> main
    def get(self, request):
        data_response = {"msg": "Método GET no permitido"}
        return Response(data_response, status.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request):
<<<<<<< HEAD
        # Recuperamos las credenciales y autenticamos al usuario
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        # Si es correcto añadimos a la request la información de sesión
        if user:
            login(request, user)
            return Response({
            "user": UserSerializer(user).data,
            "message": LOGIN_OK
            }, status=status.HTTP_200_OK)

        # Si no es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)"""






class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        return data

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)




=======
        code_employee = request.data.get("code_employee", None)
        password = request.data.get("password", None)

        if code_employee is None or password is None:
            return Response(LOGIN_CREDENTIALS_REQUIRED_ERROR, status=status.HTTP_400_BAD_REQUEST)
        else: 
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

# @permission_classes([IsAuthenticated])
class LogoutView(GenericAPIView):
    def post(self, request):
        try:
            token_request = request.headers.get('token', None)
            token = Token.objects.get(key=token_request)
            if token: 
                user = CustomUser.objects.filter(auth_token=token).first()
                user.auth_token.delete()
                logout(request)
                return Response({"msg": "Sesion finalizada"},status=status.HTTP_200_OK)
            return Response({"error":"El usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)   
        except:
            return Response({"error":"El usuario no existe"}, status=status.HTTP_400_BAD_REQUEST)   




class SignUpView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(user, context = self.get_serializer_context()).data,
                "message": SIGNUP_OK
            },
        )

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def disableUser(request, user_id):
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


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
        serializer = UserSerializerUpdate(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except CustomUser.DoesNotExist:
        return Response({"error": "No existe un usuario con ese id"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUsers(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePassword(request, user_id):
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
def request_recovery_password(request):
    email = request.data.get("email", None)
    if email is None:
        return Response({"error": "El email es obligatorio"}, status.HTTP_400_BAD_REQUEST)

    try:
        user = CustomUser.objects.get(email=email)
        # if user:
        Token.objects.get_or_create(user=user)
        message = 'Se le han enviado las instrucciones a su correo electrónico para recuperar su contraseña. Debería recibirlo en un lapso de tiempo corto. Sino recibió correo electrónico alguno, por favor, asegurese de que haya ingresado su dirección de correo electrónico correctamente, también revise su carpeta de spam.'
        recovery_link = 'enlace_de_recuperacion_de_contraseña_aqui'
        message_email = f'Para establecer una nueva contraseña, de click en el siguiente enlace: {recovery_link}'
            
        send_mail( 
            'Recuperar contraseña',# 'Subject here',
            message_email,# 'Here is the message.',
            settings.EMAIL_HOST_USER,# 'from@example.com',
            [email],# ['to@example.com'],
            fail_silently=False,
        )

        return Response({"msg": message})
    except:
        return Response({"error":"El email no corresponde a ningún usuario registrado"})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def changePassword(request, user_id):
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

# @api_view(['POST']) 
# def send_mail_message(request):
#     send_mail( 
#         'Mensaje de prueba',# 'Subject here',
#         'Este es un email de prueba, enviado mediante django',# 'Here is the message.',
#         settings.EMAIL_HOST_USER,# 'from@example.com',
#         ['sigma4726spring@gmail.com'],# ['to@example.com'],
#         fail_silently=False,
#     )
#     return Response({"msg":"Email enviado exitosamente"})
>>>>>>> main


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mensaje(request):
<<<<<<< HEAD
     return Response({"msg":"Hola Mundo"})
=======
    return Response({"msg":"Hola Mundo"})
>>>>>>> main
