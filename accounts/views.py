from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy

from .forms import SignUpForm, UserUpdateForm, UserProfileUpdateForm
from .models import User

class Profile(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

class UserEditView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
    def post(self, request):
        user = get_object_or_404(User, pk=request.user.id)
        u_form = UserUpdateForm(request.POST, instance=user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            if User.objects.exclude(id=request.user.id).filter(email=u_form.cleaned_data['email']):
                messages.error(request, "A user with this email already exist!")
                return render(request, 'registration/edit_profile.html', {'u_form':u_form, 'p_form': p_form })
            u_form.save()
            p_form.save()
            return redirect('home')
        u_form = UserUpdateForm()
        p_form = UserProfileUpdateForm()
        return render(request, 'registration/edit_profile.html', {'u_form':u_form , 'p_form': p_form})


def create_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email=form.cleaned_data['email']):
                messages.error(request, "A user with this email already exist!")
                return render(request, 'registration/signup.html', {'form':form })
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form':form })
    return render(request, 'registration/signup.html', {'form':form })


@login_required(redirect_field_name='home')
def delete_user(request):
    if request.method == 'POST':
        user = get_object_or_404(User, pk=request.user.id)
        user.delete()
        messages.success(request, 'Your account have been deleted!')
        return redirect('home')
    return render(request, 'registration/delete_profile.html')

