from django.shortcuts import render

# Create your views here.
def student_login(request):
    return render(request, 'login/login.html')