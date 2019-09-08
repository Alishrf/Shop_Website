from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User



def register(request):
    if request.POST:
        name = request.POST['c_fname']
        family_name = request.POST['c_lname']
        email = request.POST['c_email']
        password1 = request.POST['c_password']
        password2 = request.POST['c_password2']
        if password1==password2 :
            has_email = User.objects.filter(email = email)
            if has_email:
                messages.error(request,'This Email Already Use')   
                return  redirect(register)
            else:
                user = User.objects.create_user(first_name = name , last_name = family_name ,
                 email = email , password = password1,username = email)
                messages.success(request , 'You Are Registered Successfully')
                return redirect(login)
        else :
            messages.error(request,'Your Passwords Aren\'t Match')   
            return  redirect(register)
    return render(request , 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['c_email']
        password = request.POST['c_password']
        user = auth.authenticate(username = email , password = password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You Are Loged In Successfully')
            return redirect(login)
        else:
            messages.error(request,'Email Or Passsword Is Not Availabe')
            return redirect(login)


    return render(request , 'accounts/login.html')
