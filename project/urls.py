from django.contrib import admin
from django.urls import path, include
from login import views as login
from register import views as register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.student_login, name='login'),
    path('', login.student_login, name='login'),
    path('register/', register.register, name='register'),
]