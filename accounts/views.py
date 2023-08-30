from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def login_view(request):
    context = {
        'page_title' : 'login'
    }

    if request.method == 'POST':
        # user = None
        username_login = request.POST['username']
        password_login = request.POST['password']

        user = authenticate(username = username_login, password = password_login)
        
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:      
            return redirect('login')
    
    return render(request,'auth/login.html', context)

def logout_view(request):
   logout(request)
   return redirect('home')