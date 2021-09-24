from django.shortcuts import redirect, render

from django.contrib import messages
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method =='POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome {username} , your account is created')
            return redirect('login')
    else:

       form=RegistrationForm()
    return render(request, 'users/register.html',{'form':form})