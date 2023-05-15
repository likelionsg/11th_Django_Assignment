from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

def login(request):
    if request.method == 'POST':
        userid = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=userid, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('list_page')
        else:
            return render(request, 'login_form.html')
    else: # GET 요청
        return render(request, 'login_form.html')
    
def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username = request.POST['id'],
            password = request.POST['password'],
            phone = request.POST['phone']
        )
        auth.login(request, user)
        return redirect('list_page')
    else:
        return render(request, 'signup.html')
    
def logout(request):
    auth.logout(request)
    return redirect('list_page')