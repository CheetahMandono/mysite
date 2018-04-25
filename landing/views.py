from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import View
from django.http import HttpResponseRedirect


def landing(request):
    return render(request, 'landing/landing.html', locals())


def base_page(request):
    return render(request, 'landing/base.html', locals())


class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "landing/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/landing/base"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('landing/base.html')
    else:
        form = SignUpForm()
    return render(request, 'landing/signup.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/landing/base")

