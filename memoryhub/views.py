from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as LogOut

import memoryhub
from .models import Memory

# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required
def home(request):
  memories = Memory.objects.filter(user=request.user)
  if memories:
    memories = reversed(memories)
  return render(request, 'home.html', {'memories': memories})

@login_required
def map(request):
    return render(request, 'map.html')

@login_required
def create(request):
  #cai nay co the dung ModelForm class de tot hon
    if request.method == 'POST':
        location, comment = request.POST.get('location'), request.POST.get('comment')
        if location and comment:
          memory = Memory(location = location, comment = comment, user = request.user)
          memory.save()
          return redirect('home')
        else:
          return render(request, 'memorycreation.html')
    else:
        return render(request, 'memorycreation.html')

@login_required
def logout(request):
  LogOut(request)
  return render(request, 'logout.html')
