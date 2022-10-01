from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreationForm



# Create your views here.

def handel_registeration(request):
    if request.method == 'POST':
      form = CreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('handel_work_request')
    else:
        form = CreationForm()
    
    context = {'form':form}
    return render(request, 'personnel/register.html', context)

# def handel_logout(request):
#   if request.method == "POST":
#     form = LoginForm(request.POST)
#     if form.is_valid():
#       form.save()
#       return redirect('handel_work_request')
#   else:
#     form= LoginForm()
  
#   context = {'form':form}
#   return render(request, 'personnel/logout.html', context)