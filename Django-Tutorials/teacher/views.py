from django.shortcuts import render,HttpResponse, redirect, reverse
from django.contrib.auth.models import User
from .models import Assign
from accounts.models import UserProfile
from accounts.forms import EditProfileForm
from questionpaper.models import WritingTest, ListeningTest, ReadingTest
from accounts.forms import RegistrationForm, UserProfileForm
# Create your views here.
def home(request):
    if request.method == "POST":
        Student = request.POST.get("Student")
        Test = request.POST.get("Test")
        stat = "Assiged"
        Assign.objects.create(Student=Student, test_name=Test, status=stat)
        Assign.objects.update()
        return redirect(reverse('teacher:home'))
    elif request.user.userprofile.profile == "T":
        usr = UserProfile.objects.get(user=request.user)
        org = usr.Organisation
        usr = UserProfile.objects.filter(Organisation=org)
        read = ReadingTest.objects.all()
        listen = ListeningTest.objects.all()
        write = WritingTest.objects.all()
        assign = Assign.objects.all()
        args = {'user':usr, 'read':read, 'Listen':listen, 'write':write, 'assign':assign}
        return render(request, 'panel.html', args)
    else:
        return HttpResponse("<h1>You are not authorised to view this page</h1>")
def addStudent(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            userr = form.save()
            userrr = User.objects.get(username=userr)
            userid = userrr.id
            phone = request.POST.get("phone")
            user = UserProfile.objects.get(user=request.user)
            org = user.Organisation
            profile = "S"
            UserProfile.objects.create(user_id=userid, phone=phone, profile=profile, Organisation=org)
            return redirect(reverse('teacher:addStudent'))
        else:
            return HttpResponse("form invalid")
    elif request.user.userprofile.profile == "T":
        form1 = RegistrationForm()
        form2 = UserProfileForm()
        usr=UserProfile.objects.get(user=request.user)
        org = usr.Organisation
        usrp = UserProfile.objects.filter(Organisation=org)
        args = {'form1':form1, 'form2':form2, 'usrp':usrp}
        return render(request, 'panel1.html', args)
    else:
        return HttpResponse("<h1>You are not authorised to view this page</h1>")

def delete_studentprofile(request, part_id=None):
    User.objects.filter(id=part_id).delete()
    return redirect(reverse('teacher:addStudent'))


def delete_assign(request, part_id=None):
    print(part_id)
    Assign.objects.filter(id=part_id).delete()
    return redirect(reverse('teacher:home'))
