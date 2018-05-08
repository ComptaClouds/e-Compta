activation_key = helpers.generate_activation_key(username=request.POST['username'])

subject = "TheGreatDjangoBlog Account Verification"

message = '''\n
           Please visit the following link to verify your account \n\n{0}://{1}/activate/account/?key={2}
                                   '''.format(request.scheme, request.get_host(), activation_key)

error = False

try:
    send_mail(subject, message, settings.SERVER_EMAIL, [request.POST['email']])
    messages.add_message(request, messages.INFO,
                         'Account created! Click on the link sent to your email to activate the account')

except:
    error = True
    messages.add_message(request, messages.INFO, 'Unable to send email verification. Please try again')

if not error:
    u = User.objects.create_user(
        request.POST['username'],
        request.POST['email'],
        request.POST['password1'],
        is_active=0
    )

    author = UserProfile()
    author.activation_key = activation_key
    author.user = u
    author.save()
    return redirect(reverse_lazy('register'))
    else:
    #return render(request, 'accounts/reg_form.html',
              #    {'form': form})