from django.urls import path, include
from .views import MyTokenObtainPairView, mensaje, LogoutView

urlpatterns = [
    # Auth views
    
    path('auth/users/test/', mensaje),
    path('auth/users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/users/logout/', LogoutView.as_view(), name="auth_logout")

]

#anterior path
"""path('auth/login/', LoginView.as_view(), name='auth_login'),

    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),""",