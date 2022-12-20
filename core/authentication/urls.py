from django.urls import path, include
<<<<<<< HEAD
from .views import MyTokenObtainPairView, mensaje, LogoutView

urlpatterns = [
    # Auth views
    
    path('auth/users/test/', mensaje),
    path('auth/users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/users/logout/', LogoutView.as_view(), name="auth_logout"),
]

#anterior path
"""path('auth/login/', LoginView.as_view(), name='auth_login'),

    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),""",
=======
from .views import mensaje, LoginView, LogoutView, SignUpView, disableUser, getUsers, updateUser, changePassword, request_recovery_password

urlpatterns = [
    # Auth views
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('disable-user/<int:user_id>/', disableUser),
    path('signup/', SignUpView.as_view()),
    path('get-users/', getUsers),
    path('update-user/<int:user_id>/', updateUser),
    path('change-password/<int:user_id>/', changePassword),
    path('request-recovery-password/', request_recovery_password),
    # path('send-mail-message/', send_mail_message),

    path('users/test/', mensaje),
]
>>>>>>> main
