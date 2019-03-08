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
        Assign.objects.create(Student=Student, test_name=Test)
    usr = UserProfile.objects.get(user=request.user)
    org = usr.Organisation
    usr = UserProfile.objects.filter(Organisation=org)
    read = ReadingTest.objects.all()
    listen = ListeningTest.objects.all()
    write = WritingTest.objects.all()
    assign = Assign.objects.all()
    args = {'user':usr, 'read':read, 'Listen':listen, 'write':write, 'assign':assign}
    return render(request, 'panel.html', args)

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
        else:
            return HttpResponse("form invalid")
    form1 = RegistrationForm()
    form2 = UserProfileForm()
    usr=UserProfile.objects.get(user=request.user)
    org = usr.Organisation
    usrp = UserProfile.objects.filter(Organisation=org)
    args = {'form1':form1, 'form2':form2, 'usrp':usrp}
    return render(request, 'panel1.html', args)


def delete_studentprofile(request, part_id=None):
    User.objects.filter(id=part_id).delete()
    return redirect(reverse('teacher:addStudent'))


def delete_assign(request, part_id=None):
    print(part_id)
    Assign.objects.filter(id=part_id).delete()
    return redirect(reverse('teacher:home'))
