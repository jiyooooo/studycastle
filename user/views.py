from django.views.generic import CreateView, FormView
from user.forms import UserRegisterForm
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render


# 회원가입
class UserRegister(CreateView):
    model = get_user_model()
    form_class = UserRegisterForm
    template_name = 'user/join.html'
    success_url = '/user/login/'


# 로그인
class UserLogin(LoginView):
    template_name = 'user/login.html'

    # 유효성 검증에 실패한 경우 form_invalid 메소드를 오버라이딩해서 에러 메시지를 출력
    def form_invalid(self, form):
        messages.error(self.request, '로그인에 실패하였습니다.', extra_tags='danger')
        return super().form_invalid(form)