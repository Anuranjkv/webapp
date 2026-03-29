from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def student_login(request):
    if request.method == 'POST':
        # Get data from the form
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        # Authenticate against the User database
        user = authenticate(request, username=u_name, password=p_word)

        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')  # Change 'home' to your dashboard/success URL
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'login/login.html')

    # GET request shows the login page
    return render(request, 'login/login.html')