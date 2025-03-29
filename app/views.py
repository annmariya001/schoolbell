from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login


def home(request):
    return render(request, "main_home.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        mobile_number = request.POST.get('mobile_number')  # Not used in User model
        password = request.POST.get('password')
        re_password = request.POST.get('again_password')

        if password != re_password:
            messages.error(request, "Passwords do not match.")
            return render(request, "register.html")

        if User.objects.filter(username=user_name).exists():
            messages.error(request, "Username already taken.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return render(request, "register.html")

        # Save user to Django's built-in User model
        user = User.objects.create_user(
            username=user_name,
            email=email,
            password=password
        )
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        messages.success(request, "Registration successful! 🎉 You can now log in.")
        return redirect("login")  # Change "login" to your login page URL name

    return render(request, "register.html")


def login_view(request):  # ✅ Renamed function
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')

        # Debugging: Print input values (remove in production)
        print(f"Username: {user_name}, Password: {password}")

        # Authenticate user
        user = authenticate(request, username=user_name, password=password)

        if user is not None:
            auth_login(request, user)  # ✅ Using Django's login function safely
            messages.success(request, "Login successful! 🎉")
            return render(request, "index.html")  # ✅ Use the correct name of your home URL
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")
