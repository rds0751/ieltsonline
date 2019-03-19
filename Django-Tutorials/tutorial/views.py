from django.shortcuts import redirect, HttpResponse, reverse

def login_redirect(request):
    return redirect('/account/login')

def home(request):
    if request.user.userprofile.profile == 'S':
        return redirect(reverse('student:home'))
    elif request.user.userprofile.profile == 'T':
        return redirect(reverse('teacher:home'))
    else:
        return HttpResponse("<h3>You are an unauthorised user</h3>")
