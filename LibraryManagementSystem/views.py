from django.shortcuts import render
from .models import User
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponse

# Create your views here.
def registerUser(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        
        if username and password and email:
            try:
                validate_password(password)
            except Exception as e:
                return JsonResponse({"success": False, "Error": str(e)})
            
            try:
                user = User.objects.create_user(
                    username=username, email=email, password=password
                )
                user.save()
                login(request, user)
            except Exception as e:
                if "username" in str(e):
                    return JsonResponse({"success": False, "Error": "Username already taken!"})
                elif "email" in str(e):
                    return JsonResponse({"success": False, "Error": "Email already in use!"})
                
                return JsonResponse({"success": False, "Error": "Failed to register user."})
                
            return JsonResponse({"success": True})
        return JsonResponse({"success": False, "Error": "Fields cannot be left empty!"})
    return HttpResponse("Wrong method")

def loginUser(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        username = data.get("username")
        password = data.get("password")
        
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"success": True})
            return JsonResponse({"success": False, "Error": "Invalid credentials."})
        return JsonResponse({"success": False, "Error": "Fields cannot be left empty!"})
    return HttpResponse("Wrong method")

def logoutUser(request):
    logout(request)
    return JsonResponse({"success": True})