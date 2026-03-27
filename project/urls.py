from django.contrib import admin
from django.urls import path, include
from login import views as login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login.student_login, name='student_login'),
]