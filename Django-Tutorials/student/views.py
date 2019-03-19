from django.shortcuts import render, HttpResponse
from teacher.models import Assign
# Create your views here.
def home(request):
    if request.user.userprofile.profile == 'S':
        asn = Assign.objects.filter(Student=request.user)
        args = {'asn':asn}
        return render(request, 'student_panel.html', args)
    else:
        return HttpResponse("<h4>You are not authorised to give the test as you are not a student</h4>")
