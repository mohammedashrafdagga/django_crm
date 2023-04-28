from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


def register_user(request):
    ''' register to create new account using built-in form in django '''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect('core:index')
    else:
        form = UserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})
