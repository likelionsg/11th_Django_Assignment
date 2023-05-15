from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def login(request):

    ## 로그인 비즈니스 로직 처리
    if request.method == 'POST':
        userid = request.POST['id']
        pwd = request.POST['password']
        user = auth.authenticate(request,username=userid, password=pwd)

        ## 인증된 유저가 존재한다면 로그인 시켜준다.
        ## 그리고 index로 리다이렉트 시켜준다.
        if user is not None:
            auth.login(request, user)
            return redirect('list_page')
        
        ## 인증된 유저가 존재하지 않는다면
        ## 다시 로그인 폼 화면을 가도록 해준다.
        else:

            context = {'errorMessage' : '존재하지 않는 회원정보입니다.'}
            return render(request, 'login_form.html', context)

    ## 로그인 폼 화면 주기
    elif request.method == 'GET':
        return render(request, 'login_form.html')
    

def logout(request):

    auth.logout(request)

    return redirect('list_page')


def signup(request):

    ## POST 요청 들어오면 디비에 저장해주기
    if request.method == "POST":

        username = request.POST['id']
        password = request.POST['password']
        phone = request.POST['phone']


        object = User.objects.filter(username=username, phone=phone).values()

        ## 회원 정보가 존재하면 이미 존재하는 회원이므로 동작하지 않도록 하기
        if object:
            context = {"errorMessage" : "이미 존재하는 회원정보입니다."}
            return render(request, 'signup.html', context)
        
        else:
            user = User.objects.create_user(
                username = username,
                password = password,
                phone = phone
            )

            auth.login(request, user)
            return redirect('list_page')

        

    ## GET 요청 들어오면 회원가입 폼 화면 띄워주기
    elif request.method == "GET":
        return render(request, 'signup.html')