from django.urls import path
from . import views

urlpatterns = [
   # path('register/', RegistrationView.as_view , name="registration"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup , name="signup")
]