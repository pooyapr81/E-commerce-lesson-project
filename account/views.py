from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import Userregister, Userlogin
from .models import Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as djviews
from django.urls import reverse_lazy


class rigesteruser(View):
    form_class = Userregister
    template_name = 'account/register.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'], cd['email'], cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request, 'register successfully', 'success')
            return redirect('home:home')
        return render(request, self.template_name, {'form': form})


class loginuser(View):
    form_class = Userlogin
    template_name = 'account/login.html'

    def setup(self, request, *args, **kwargs):
        self.next = request.GET.get('next', None)
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'welcome!!', 'success')
                if self.next:
                    return redirect(self.next)
                return redirect('home:home')
            else:
                messages.error(request, 'password is wrong or you not rigestered yet ', 'danjer')
                return render(request, self.template_name, {'form': form})


class logoutuser(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'logout successfully')
        return redirect('home:home')


class profileuser(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        return render(request, 'accounts/profile.html', {'user': user})
