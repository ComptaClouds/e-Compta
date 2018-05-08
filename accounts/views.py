
from accounts.forms import RegistrationForm,EditProfileForm,HomeForm,UserForm,ProfileForm
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db import transaction
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import redirect, get_object_or_404, reverse, Http404
from django.urls import reverse_lazy
from django.contrib import messages
from django.template import RequestContext
from .models import UserProfile
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from accounts.tokens import account_activation_token

def home(request):

    return render(request, 'accounts/home.html')

def logout(request):

    return render(request, 'accounts/logout.html')

#vue inscription
def registerdd(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
           #activation par mail

           #activation par mail

            form.save()
            return redirect('home')
        else:
            return render(request, 'accounts/reg_form.html',
                          {'form': form})
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)


def registerProfile(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')
    else:
        form = HomeForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.userprofile.email = True
        user.save()
        logout(request)
        return redirect('home')
    else:
        return render(request, 'accounts/account_activation_invalid.html')




def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')


@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST, request.FILES)
        profile_form = HomeForm(request.POST, request.FILES or None)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.refresh_from_db()  # This will load the Profile created by the Signal
            profile_form = HomeForm(request.POST, instance=user.userprofile)  # Reload the profile form with the profile instance
            profile_form.full_clean()  # Manually clean the form this time. It is implicitly called by "is_valid()" method
            profile_form.save()  # Gracefully save the form
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('accounts/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect(reverse_lazy('account_activation_sent'))

    else:
        user_form = RegistrationForm()
        profile_form = HomeForm()
    return render(request, 'accounts/reg_form.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
@transaction.atomic
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, request.FILES, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES or None, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('/account/profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def registerss(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.userprofile.contact = form.cleaned_data.get('contact')
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=password)
            login(request, user)
            return redirect('/account')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/reg_form.html', {'form': form})



#vue voir profile
def view_profile(request):
    args = {'user':request.user}
    return render(request, 'accounts/profile.html', args)


#vue modifier profile
@login_required
def edit_profilec(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/account/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

#vue changer mot de pass
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():

            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile')
        else:
            return redirect('/account/change-password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)








