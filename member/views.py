from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('index')
    else:
        form = UserForm()
    return render(request, 'member/signup.html', {'form': form})


from .models import Member
from django.utils import timezone
from django.http import HttpResponse
def signup_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        user_name = request.POST.get('user_name')
        m = Member(
            user_id=user_id, user_pw=user_pw, user_name=user_name)
        m.date_joined = timezone.now()
        m.save()
        return HttpResponse(
        '가입 완료<br>%s %s %s' % (user_id, user_pw, user_name))
    else:
        return render(request, 'member/signup_custom.html')


def login_custom(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user_pw = request.POST.get('user_pw')
        try:
            m = Member.objects.get(user_id=user_id, user_pw=user_pw)
        except:
            return HttpResponse("아이디 비밀번호를 확인하세요")
        else:
            request.session['user_id']=m.user_id
            request.session['user_name']=m.user_name
            request.session['id']=m.id

        # 회원정보 조회 실패 시 예외 발생
        return redirect('member:login')
    else:
        return render(request, 'member/login_custom.html')



def logout_custom(request):
    del request.session['user_id']
    del request.session['user_name']
    del request.session['id']

    request.session.flush()
    return redirect('member:login_custom')