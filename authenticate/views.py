from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import PasswordChangeForm

from django.contrib import messages

from .forms import SignUpForm, EditProfileForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def login_user(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # redirect to success page
            return redirect('home')
        else:
            # Redirect an 'invalid login' error message
            messages.success(request, ('Error loggining In.... Please try again'))
            return redirect('login')
    else:
        return render(request, 'login.html')
    
    

def logout_user(request):
    logout(request)
    # Redirect to a success page.
    messages.success(request, ('You have been logged out ...'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have successfully registered......'))
            return redirect('home')
    else:
        form = SignUpForm()
    context = {'form': form}
    
    return render(request, 'register.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Successfully Edited Your Profile'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        context = {'form': form}
    return render(request, 'edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Successfully Edited Your Password'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'change_password.html', context)