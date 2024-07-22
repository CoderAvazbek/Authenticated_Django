from django.urls import path
from .views import login_view, logount, home, register

urlpatterns = [
    path('', home, name="home"),

    path('login/', login_view, name="login"),
    path('register/', register, name="register"),
    path('logount/', logount, name="logount"),
]