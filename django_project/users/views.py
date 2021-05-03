from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm       #for form creation
from django.contrib import messages  #to display message for form creation error or success
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm , UserUpdateForm, ProfileUpdateForm
#now we inherted that form with email also as field

#it is very commmon so it is already existing in django



'''
#initially it was there from UserCreationForm
#but now we also added email as field so we will make changes
#replace UserCreationForm by UserRegisterForm
#and we can also reomve "from django.contrib.auth.forms import UserCreationForm" from top, bcz we are not creating form here
# we are inheriting the form from UserRegistrerationForm

def register(request):
    if request.method =='POST':        #to validate the data when we press submit button
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()      #save password for that username
            username = form.cleaned_data.get('username')  #get username from validated data
            messages.success(request, f'Account created for {username}!')  #flash message
                        #now check for flashmessage on which page..bcz we extended base.html
            return redirect('blog-home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html',{'form':form})
'''

def register(request):
    if request.method =='POST':        #to validate the data when we press submit button
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()      #save password for that username
            username = form.cleaned_data.get('username')  #get username from validated data
            messages.success(request, f'Your account have been created! You are now able to login')  #flash message
                        #now check for flashmessage on which page..bcz we extended base.html
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html',{'form':form})



@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)