from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        # Get data from the 'name' attributes in your HTML
        username = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 1. Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'register/registeration.html')

        # 2. Create the user in the database
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=password
        )
        user.save()

        # 3. Success! Send them to the login page
        messages.success(request, "Registration successful! Please login.")
        return redirect('login') 

    # If it's a GET request, just display the page
    return render(request, 'register/registeration.html')
def home(request):
    return render(request, 'home.html')
