from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
def login(request):
    if request.method == 'POST':
        userid = request.POST['id']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd) # 인증
        if user is not None:
            # 로그인 성공 절차
            auth.login(request, user)
            return redirect('list_page')
        else:
            return render(request, 'login_form.html')
            # 로그인 실패
    else: # GET
        return render(request, 'login_form.html')
        
def signup(request):
    if request.method == 'POST':
        new_user = User.objects.create_user(
            username=request.POST['id'], 
            password=request.POST['password'] ,
            phone=request.POST['phone']
        )
        auth.login(request, new_user)
        return redirect('list_page')
    else: 
        return render(request, 'signup.html')
    
def logout(request):
    auth.logout(request)
    return redirect('list_page')