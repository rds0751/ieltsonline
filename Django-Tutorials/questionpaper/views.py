from django.shortcuts import render, HttpResponse
from .models import ReadingTest, ListeningTest, WritingTest, WritingAnswer, ReadingAnswer, ListeningAnswer
from teacher.models import Assign
from reading.models import MCQ, yesNoNotGiven, Summary, Fillup, Matching
from reading.models import yesNoNotGivenQues, MCQQues, FillupQue
from listening.models import MCQ as MCQl, Summary as Summaryl, MapMatch as MapMatchl, Fillup as Fillupl, Matching as Matchingl
from listening.models import MCQQues as MCQQuesl, MapMatchQues as MapMatchQuesl, FillupQue as FillupQuel
from writing.models import Writing
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return HttpResponse("WELCOME TO IELTS QUESTION PAPER SECTION")


def ReadingPaper(request, part_id):
    if request.method == 'POST':
        student = User.objects.get(username=request.user)
        if request.POST.get('test_name'):
            test_name = request.POST.get('test_name')
            if request.POST.get('ysnida[0]'):
                ysn_ida0 = request.POST.get('ysnida[0]')
                ansa0 = request.POST.get('ysna[0]')
            if request.POST.get('ysnida[1]'):
                ysn_ida1 = request.POST.get('ysnida[1]')
                ansa1 = request.POST.get('ysna[1]')
            if request.POST.get('ysnida[2]'):
                ysn_ida2 = request.POST.get('ysnida[2]')
                ansa2 = request.POST.get('ysna[2]')
            if request.POST.get('ysnida[3]'):
                ysn_ida3 = request.POST.get('ysnida[3]')
                ansa3 = request.POST.get('ysna[3]')
            if request.POST.get('ysnida[4]'):
                ysn_ida4 = request.POST.get('ysnida[4]')
                ansa4 = request.POST.get('ysna[4]')
            if request.POST.get('ysnida[5]'):
                ysn_ida5 = request.POST.get('ysnida[5]')
                ansa5 = request.POST.get('ysna[5]')

            if request.POST.get('suma'):
                sum_ida = request.POST.get('suma')
            if request.POST.get('suma0'):
                suma0 = request.POST.get('suma0')
            if request.POST.get('suma1'):
                suma1 = request.POST.get('suma1')
            if request.POST.get('suma2'):
                suma2 = request.POST.get('suma2')
            if request.POST.get('suma3'):
                suma3 = request.POST.get('suma3')
            if request.POST.get('suma4'):
                suma4 = request.POST.get('suma4')
            if request.POST.get('suma5'):
                suma5 = request.POST.get('suma5')

            if request.POST.get('mcqa[0]'):
                mcq_ida = request.POST.get('mcqa[0]')
            if request.POST.get('mcqqa[0]'):
                mcqa0 = request.POST.get('mcqqa[0]')

            if request.POST.get('fillup_ida[0]'):
                fillup_ida0 = request.POST.get('fillup_ida[0]')
            if request.POST.get('fillupa[0]'):
                fillupa0 = request.POST.get('fillupa[0]')
            if request.POST.get('fillup_ida[1]'):
                fillup_ida1 = request.POST.get('fillup_ida[1]')
            if request.POST.get('fillupa[1]'):
                fillupa1 = request.POST.get('fillupa[1]')
            if request.POST.get('fillup_ida[2]'):
                fillup_ida2 = request.POST.get('fillup_ida[2]')
            if request.POST.get('fillupa[2]'):
                fillupa2 = request.POST.get('fillupa[2]')

            if request.POST.get('mat_ida'):
                mat_ida = request.POST.get('mat_ida')
            if request.POST.get('mata0'):
                mata0 = request.POST.get('mata0')
            else:
                mata0 = ""
            if request.POST.get('mata1'):
                mata1 = request.POST.get('mata1')
            else:
                mata1 = ""
            if request.POST.get('mata2'):
                mata2 = request.POST.get('mata2')
            else:
                mata2 = ""
            if request.POST.get('mata3'):
                mata3 = request.POST.get('mata3')
            else:
                mata3 = ""



            if request.POST.get('ysnidb[0]'):
                ysn_idb0 = request.POST.get('ysnidb[0]')
                ansb0 = request.POST.get('ysnb[0]')
            if request.POST.get('ysnidb[1]'):
                ysn_idb1 = request.POST.get('ysnidb[1]')
                ansb1 = request.POST.get('ysnb[1]')
            if request.POST.get('ysnidb[2]'):
                ysn_idb2 = request.POST.get('ysnidb[2]')
                ansb2 = request.POST.get('ysnb[2]')
            if request.POST.get('ysnidb[3]'):
                ysn_idb3 = request.POST.get('ysnidb[3]')
                ansb3 = request.POST.get('ysnb[3]')
            if request.POST.get('ysnidb[4]'):
                ysn_idb4 = request.POST.get('ysnidb[4]')
                ansb4 = request.POST.get('ysnb[4]')
            if request.POST.get('ysnidb[5]'):
                ysn_idb5 = request.POST.get('ysnidb[5]')
                ansb5 = request.POST.get('ysnb[5]')

            if request.POST.get('sumb'):
                sum_idb = request.POST.get('sumb')
            if request.POST.get('sumb0'):
                sumb0 = request.POST.get('sumb0')
            if request.POST.get('sumb1'):
                sumb1 = request.POST.get('sumb1')
            if request.POST.get('sumb2'):
                sumb2 = request.POST.get('sumb2')
            if request.POST.get('sumb3'):
                sumb3 = request.POST.get('sumb3')
            if request.POST.get('sumb4'):
                sumb4 = request.POST.get('sumb4')
            if request.POST.get('sumb5'):
                sumb5 = request.POST.get('sumb5')

            if request.POST.get('mcqb[0]'):
                mcq_idb = request.POST.get('mcqb[0]')
            if request.POST.get('mcqqb[0]'):
                mcqb0 = request.POST.get('mcqqb[0]')

            if request.POST.get('fillup_idb[0]'):
                fillup_idb0 = request.POST.get('fillup_idb[0]')
            if request.POST.get('fillupb[0]'):
                fillupb0 = request.POST.get('fillupb[0]')
            if request.POST.get('fillup_idb[1]'):
                fillup_idb1 = request.POST.get('fillup_idb[1]')
            if request.POST.get('fillupb[1]'):
                fillupb1 = request.POST.get('fillupb[1]')
            if request.POST.get('fillup_idb[2]'):
                fillup_idb2 = request.POST.get('fillup_idb[2]')
            if request.POST.get('fillupb[2]'):
                fillupb2 = request.POST.get('fillupb[2]')

            if request.POST.get('mat_idb'):
                mat_idb = request.POST.get('mat_idb')
            if request.POST.get('matb0'):
                matb0 = request.POST.get('matb0')
            else:
                matb0 = ""
            if request.POST.get('matb1'):
                matb1 = request.POST.get('matb1')
            else:
                matb1 = ""
            if request.POST.get('matb2'):
                matb2 = request.POST.get('matb2')
            else:
                matb2 = ""
            if request.POST.get('matb3'):
                matb3 = request.POST.get('matb3')
            else:
                matb3 = ""


            if request.POST.get('ysnidc[0]'):
                ysn_idc0 = request.POST.get('ysnidc[0]')
                ansc0 = request.POST.get('ysnc[0]')
            if request.POST.get('ysnidc[1]'):
                ysn_idc1 = request.POST.get('ysnidc[1]')
                ansc1 = request.POST.get('ysnc[1]')
            if request.POST.get('ysnidc[2]'):
                ysn_idc2 = request.POST.get('ysnidc[2]')
                ansc2 = request.POST.get('ysnc[2]')
            if request.POST.get('ysnidc[3]'):
                ysn_idc3 = request.POST.get('ysnidc[3]')
                ansc3 = request.POST.get('ysnc[3]')
            if request.POST.get('ysnidc[4]'):
                ysn_idc4 = request.POST.get('ysnidc[4]')
                ansc4 = request.POST.get('ysnc[4]')
            if request.POST.get('ysnidc[5]'):
                ysn_idc5 = request.POST.get('ysnidc[5]')
                ansc5 = request.POST.get('ysnc[5]')

            if request.POST.get('sumc'):
                sum_idc = request.POST.get('sumc')
            if request.POST.get('sumc0'):
                sumc0 = request.POST.get('sumc0')
            if request.POST.get('sumc1'):
                sumc1 = request.POST.get('sumc1')
            if request.POST.get('sumc2'):
                sumc2 = request.POST.get('sumc2')
            if request.POST.get('sumc3'):
                sumc3 = request.POST.get('sumc3')
            if request.POST.get('sumc4'):
                sumc4 = request.POST.get('sumc4')
            if request.POST.get('sumc5'):
                sumc5 = request.POST.get('sumc5')

            if request.POST.get('mcqc[0]'):
                mcq_idc = request.POST.get('mcqc[0]')
            if request.POST.get('mcqqc[0]'):
                mcqc0 = request.POST.get('mcqqc[0]')

            if request.POST.get('fillup_idc[0]'):
                fillup_idc0 = request.POST.get('fillup_idc[0]')
            if request.POST.get('fillupc[0]'):
                fillupc0 = request.POST.get('fillupc[0]')
            if request.POST.get('fillup_idc[1]'):
                fillup_idc1 = request.POST.get('fillup_idc[1]')
            if request.POST.get('fillupc[1]'):
                fillupc1 = request.POST.get('fillupc[1]')
            if request.POST.get('fillup_idc[2]'):
                fillup_idc2 = request.POST.get('fillup_idc[2]')
            if request.POST.get('fillupc[2]'):
                fillupc2 = request.POST.get('fillupc[2]')

            if request.POST.get('mat_idc'):
                mat_idc = request.POST.get('mat_idc')
            if request.POST.get('matc0'):
                matc0 = request.POST.get('matc0')
            else:
                matc0 = ""
            if request.POST.get('matc1'):
                matc1 = request.POST.get('matc1')
            else:
                matc1 = ""
            if request.POST.get('matc2'):
                matc2 = request.POST.get('matc2')
            else:
                matc2 = ""
            if request.POST.get('matc3'):
                matc3 = request.POST.get('matc3')
            else:
                matc3 = ""


            if request.POST.get('ysnidd[0]'):
                ysn_idd0 = request.POST.get('ysnidd[0]')
                ansd0 = request.POST.get('ysnd[0]')
            if request.POST.get('ysnidd[1]'):
                ysn_idd1 = request.POST.get('ysnidd[1]')
                ansd1 = request.POST.get('ysnd[1]')
            if request.POST.get('ysnidd[2]'):
                ysn_idd2 = request.POST.get('ysnidd[2]')
                ansd2 = request.POST.get('ysnd[2]')
            if request.POST.get('ysnidd[3]'):
                ysn_idd3 = request.POST.get('ysnidd[3]')
                ansd3 = request.POST.get('ysnd[3]')
            if request.POST.get('ysnidd[4]'):
                ysn_idd4 = request.POST.get('ysnidd[4]')
                ansd4 = request.POST.get('ysnd[4]')
            if request.POST.get('ysnidd[5]'):
                ysn_idd5 = request.POST.get('ysnidd[5]')
                ansd5 = request.POST.get('ysnd[5]')

            if request.POST.get('sumd'):
                sum_idd = request.POST.get('sumd')
            if request.POST.get('sumd0'):
                sumd0 = request.POST.get('sumd0')
            if request.POST.get('sumd1'):
                sumd1 = request.POST.get('sumd1')
            if request.POST.get('sumd2'):
                sumd2 = request.POST.get('sumd2')
            if request.POST.get('sumd3'):
                sumd3 = request.POST.get('sumd3')
            if request.POST.get('sumd4'):
                sumd4 = request.POST.get('sumd4')
            if request.POST.get('sumd5'):
                sumd5 = request.POST.get('sumd5')

            if request.POST.get('mcqd[0]'):
                mcq_idd = request.POST.get('mcqd[0]')
            if request.POST.get('mcqqd[0]'):
                mcqd0 = request.POST.get('mcqqd[0]')

            if request.POST.get('fillup_idd[0]'):
                fillup_idd0 = request.POST.get('fillup_idd[0]')
            if request.POST.get('fillupd[0]'):
                fillupd0 = request.POST.get('fillupd[0]')
            if request.POST.get('fillup_idd[1]'):
                fillup_idd1 = request.POST.get('fillup_idd[1]')
            if request.POST.get('fillupd[1]'):
                fillupd1 = request.POST.get('fillupd[1]')
            if request.POST.get('fillup_idd[2]'):
                fillup_idd2 = request.POST.get('fillup_idd[2]')
            if request.POST.get('fillupd[2]'):
                fillupd2 = request.POST.get('fillupd[2]')

            if request.POST.get('mat_idc'):
                mat_idd = request.POST.get('mat_idd')
            if request.POST.get('matd0'):
                matd0 = request.POST.get('matd0')
            else:
                matd0 = ""
            if request.POST.get('matd1'):
                matd1 = request.POST.get('matd1')
            else:
                matd1 = ""
            if request.POST.get('matd2'):
                matd2 = request.POST.get('matd2')
            else:
                matd2 = ""
            if request.POST.get('matd3'):
                matd3 = request.POST.get('matd3')
            else:
                matd3 = ""

            ReadingAnswer.objects.create(student=student, test_name=test_name,
                                         ysn_ida0=ysn_ida0, ysna0=ansa0, ysn_ida1=ysn_ida1, ysna1=ansa1, ysn_ida2=ysn_ida2, ysna2=ansa2, ysn_ida3=ysn_ida3, ysna3=ansa3, ysn_ida4=ysn_ida4, ysna4=ansa4, ysn_ida5=ysn_ida5, ysna5=ansa5,
                                         sum_ida=sum_ida, suma0=suma0, suma1=suma1, suma2=suma2, suma3=suma3, suma4=suma4, suma5=suma5,
                                         mcq_ida=mcq_ida, mcqa0=mcqa0,
                                         fillup_ida0 = fillup_ida0, fillup_ida1 = fillup_ida1, fillup_ida2 = fillup_ida2, fillupa0=fillupa0, fillupa1=fillupa1, fillupa2=fillupa2,
                                         mat_ida=mat_ida, mata0=mata0, mata1=mata1, mata2=mata2, mata3=mata3,
                                         ysn_idb0=ysn_idb0, ysnb0=ansb0, ysn_idb1=ysn_idb1, ysnb1=ansb1,
                                         ysn_idb2=ysn_idb2, ysnb2=ansb2, ysn_idb3=ysn_idb3, ysnb3=ansb3,
                                         ysn_idb4=ysn_idb4, ysnb4=ansb4, ysn_idb5=ysn_idb5, ysnb5=ansb5,
                                         sum_idb=sum_idb, sumb0=sumb0, sumb1=sumb1, sumb2=sumb2, sumb3=sumb3,
                                         sumb4=sumb4, sumb5=sumb5,
                                         mcq_idb=mcq_idb, mcqb0=mcqb0,
                                         fillup_idb0=fillup_idb0, fillup_idb1=fillup_idb1, fillup_idb2=fillup_idb2,
                                         fillupb0=fillupb0, fillupb1=fillupb1, fillupb2=fillupb2,
                                         mat_idb=mat_idb, matb0=matb0, matb1=matb1, matb2=matb2, matb3=matb3,
                                         ysn_idc0=ysn_idc0, ysnc0=ansc0, ysn_idc1=ysn_idc1, ysnc1=ansc1,
                                         ysn_idc2=ysn_idc2, ysnc2=ansc2, ysn_idc3=ysn_idc3, ysnc3=ansc3,
                                         ysn_idc4=ysn_idc4, ysnc4=ansc4, ysn_idc5=ysn_idc5, ysnc5=ansc5,
                                         sum_idc=sum_idc, sumc0=sumc0, sumc1=sumc1, sumc2=sumc2, sumc3=sumc3,
                                         sumc4=sumc4, sumc5=sumc5,
                                         mcq_idc=mcq_idc, mcqc0=mcqc0,
                                         fillup_idc0=fillup_idc0, fillup_idc1=fillup_idc1, fillup_idc2=fillup_idc2,
                                         fillupc0=fillupc0, fillupc1=fillupc1, fillupc2=fillupc2,
                                         mat_idc=mat_idc, matc0=matc0, matc1=matc1, matc2=matc2, matc3=matc3,
                                         ysn_idd0=ysn_idd0, ysnd0=ansd0, ysn_idd1=ysn_idd1, ysnd1=ansd1,
                                         ysn_idd2=ysn_idd2, ysnd2=ansd2, ysn_idd3=ysn_idd3, ysnd3=ansd3,
                                         ysn_idd4=ysn_idd4, ysnd4=ansd4, ysn_idd5=ysn_idd5, ysnd5=ansd5,
                                         sum_idd=sum_idd, sumd0=sumd0, sumd1=sumd1, sumd2=sumd2, sumd3=sumd3,
                                         sumd4=sumd4, sumd5=sumd5,
                                         mcq_idd=mcq_idd, mcqd0=mcqd0,
                                         fillup_idd0=fillup_idd0, fillup_idd1=fillup_idd1, fillup_idd2=fillup_idd2,
                                         fillupd0=fillupd0, fillupd1=fillupd1, fillupd2=fillupd2,
                                         mat_idd=mat_idd, matd0=matd0, matd1=matd1, matd2=matd2, matd3=matd3,
                                         )
            return HttpResponse("<h4>aubmitted your test</h4>")
    else:
        usr = Assign.objects.filter(Student=request.user)
        pa_id = part_id
        test = "Reading Test "+part_id
        count = 0
        for i in usr:
            if i.test_name == test:
                count = 1
                passage = ReadingTest.objects.filter(id=pa_id)
                mcq = MCQ.objects.all()
                mcqques = MCQQues.objects.all()
                yesno = yesNoNotGiven.objects.all()
                yesnoques = yesNoNotGivenQues.objects.all()
                summary = Summary.objects.all()
                fillup = Fillup.objects.all()
                fillupques = FillupQue.objects.all()
                matching = Matching.objects.all()
                args = {'passage': passage, 'mcq':mcq, 'mcqques': mcqques, 'yesno':yesno, 'yesnoques':yesnoques,
                        'summary': summary, 'fillup': fillup, 'fillupques':fillupques, 'matching': matching, 'part':pa_id}
                return render(request, 'ReadingTest.html', args)
        if count == 0:
            return HttpResponse("<h1>you are not authurised to give this test ask. Ask your teacher to allot you the test</h1>")

def ListeningPaper(request, part_id):
    if request.method == "POST":
        student = User.objects.get(username=request.user)
        if request.POST.get('test_name'):
            test_name = request.POST.get('test_name')
            if request.POST.get('fillup_id[0]'):
                fillup_id0 = request.POST.get('fillup_id[0]')
            if request.POST.get('fillup[0]'):
                fillup0 = request.POST.get('fillup[0]')
            if request.POST.get('fillup_id[1]'):
                fillup_id1 = request.POST.get('fillup_id[1]')
            if request.POST.get('fillup[1]'):
                fillup1 = request.POST.get('fillup[1]')
            if request.POST.get('fillup_id[2]'):
                fillup_id2 = request.POST.get('fillup_id[2]')
            if request.POST.get('fillup[2]'):
                fillup2 = request.POST.get('fillup[2]')
            if request.POST.get('fillup_id[3]'):
                fillup_id3 = request.POST.get('fillup_id[2]')
            if request.POST.get('fillup[3]'):
                fillup3 = request.POST.get('fillup[3]')

            if request.POST.get('mcq[0]'):
                mcq_id = request.POST.get('mcq[0]')
            if request.POST.get('mcqq[0]'):
                mcq0 = request.POST.get('mcqq[0]')


            if request.POST.get('map[0]'):
                map_id0 = request.POST.get('map[0]')
            if request.POST.get('mapp[0]'):
                map0 = request.POST.get('mapp[0]')
            else:
                map0 = ""
            if request.POST.get('map[1]'):
                map_id1 = request.POST.get('map[1]')
            if request.POST.get('mapp[1]'):
                map1 = request.POST.get('mapp[1]')
            else:
                map1 = ""
            if request.POST.get('map[2]'):
                map_id2 = request.POST.get('map[2]')
            if request.POST.get('mapp[2]'):
                map2 = request.POST.get('mapp[2]')
            else:
                map2 = ""


            if request.POST.get('sum'):
                sum_id = request.POST.get('sum')
            if request.POST.get('sum0'):
                sum0 = request.POST.get('sum0')
            if request.POST.get('sum1'):
                sum1 = request.POST.get('sum1')
            if request.POST.get('sum2'):
                sum2 = request.POST.get('sum2')
            if request.POST.get('sum3'):
                sum3 = request.POST.get('sum3')
            if request.POST.get('sum4'):
                sum4 = request.POST.get('sum4')
            if request.POST.get('sum5'):
                print("into")
                sum5 = request.POST.get('sum5')
            else:
                sum5 = ""

            if request.POST.get('mat_id'):
                mat_id = request.POST.get('mat_id')
            if request.POST.get('mat0'):
                mat0 = request.POST.get('mat0')
            else:
                mat0 = ""
            if request.POST.get('mat1'):
                mat1 = request.POST.get('mat1')
            else:
                mat1 = ""
            if request.POST.get('mat2'):
                mat2 = request.POST.get('mat2')
            else:
                mat2 = ""

            if request.POST.get('fillup_idb[0]'):
                fillup_idb0 = request.POST.get('fillup_idb[0]')
            if request.POST.get('fillupb[0]'):
                fillupb0 = request.POST.get('fillupb[0]')
            if request.POST.get('fillup_idb[1]'):
                fillup_idb1 = request.POST.get('fillup_idb[1]')
            if request.POST.get('fillupb[1]'):
                fillupb1 = request.POST.get('fillupb[1]')
            if request.POST.get('fillup_idb[2]'):
                fillup_idb2 = request.POST.get('fillup_idb[2]')
            if request.POST.get('fillupb[2]'):
                fillupb2 = request.POST.get('fillupb[2]')

            if request.POST.get('mcqb[0]'):
                mcq_idb = request.POST.get('mcqb[0]')
            if request.POST.get('mcqqb[0]'):
                mcqb0 = request.POST.get('mcqqb[0]')

            if request.POST.get('mapb[0]'):
                map_idb0 = request.POST.get('mapb[0]')
            if request.POST.get('mappb[0]'):
                mapb0 = request.POST.get('mappb[0]')
            if request.POST.get('mapb[1]'):
                map_idb1 = request.POST.get('mapb[1]')
            if request.POST.get('mappb[1]'):
                mapb1 = request.POST.get('mappb[1]')
            if request.POST.get('mapb[2]'):
                map_idb2 = request.POST.get('mapb[2]')
            if request.POST.get('mappb[2]'):
                mapb2 = request.POST.get('mappb[2]')

            if request.POST.get('sumb'):
                sum_idb = request.POST.get('sumb')
            if request.POST.get('sumb0'):
                sumb0 = request.POST.get('sumb0')
            if request.POST.get('sumb1'):
                sumb1 = request.POST.get('sumb1')
            if request.POST.get('sumb2'):
                sumb2 = request.POST.get('sumb2')
            if request.POST.get('sumb3'):
                sumb3 = request.POST.get('sumb3')
            if request.POST.get('sumb4'):
                sumb4 = request.POST.get('sumb4')
            if request.POST.get('sumb5'):
                sumb5 = request.POST.get('sumb5')
            else:
                sumb5=""

            if request.POST.get('mat_idb'):
                mat_idb = request.POST.get('mat_idb')
            if request.POST.get('matb0'):
                matb0 = request.POST.get('matb0')
            else:
                matb0 = ""
            if request.POST.get('matb1'):
                matb1 = request.POST.get('matb1')
            else:
                matb1 = ""
            if request.POST.get('matb2'):
                matb2 = request.POST.get('matb2')
            else:
                matb2 = ""
            if request.POST.get('matb3'):
                matb3 = request.POST.get('matb3')
            else:
                matb3 = ""

            if request.POST.get('fillup_idc[0]'):
                fillup_idc0 = request.POST.get('fillup_idc[0]')
            if request.POST.get('fillupc[0]'):
                fillupc0 = request.POST.get('fillupc[0]')
            if request.POST.get('fillup_idc[1]'):
                fillup_idc1 = request.POST.get('fillup_idc[1]')
            if request.POST.get('fillupc[1]'):
                fillupc1 = request.POST.get('fillupc[1]')
            if request.POST.get('fillup_idc[2]'):
                fillup_idc2 = request.POST.get('fillup_idc[2]')
            if request.POST.get('fillupc[2]'):
                fillupc2 = request.POST.get('fillupc[2]')

            if request.POST.get('mcqc[0]'):
                mcq_idc = request.POST.get('mcqc[0]')
            if request.POST.get('mcqqc[0]'):
                mcqc0 = request.POST.get('mcqqc[0]')

            if request.POST.get('mapc[0]'):
                map_idc0 = request.POST.get('mapc[0]')
            if request.POST.get('mappc[0]'):
                mapc0 = request.POST.get('mappc[0]')
            if request.POST.get('mapc[1]'):
                map_idc1 = request.POST.get('mapc[1]')
            if request.POST.get('mappc[1]'):
                mapc1 = request.POST.get('mappc[1]')
            if request.POST.get('mapc[2]'):
                map_idc2 = request.POST.get('mapc[2]')
            if request.POST.get('mappc[2]'):
                mapc2 = request.POST.get('mappc[2]')

            if request.POST.get('sumc'):
                sum_idc = request.POST.get('sumc')
            if request.POST.get('sumc0'):
                sumc0 = request.POST.get('sumc0')
            if request.POST.get('sumc1'):
                sumc1 = request.POST.get('sumc1')
            if request.POST.get('sumc2'):
                sumc2 = request.POST.get('sumc2')
            if request.POST.get('sumc3'):
                sumc3 = request.POST.get('sumc3')
            if request.POST.get('sumc4'):
                sumc4 = request.POST.get('sumc4')
            if request.POST.get('sumc5'):
                sumc5 = request.POST.get('sumc5')
            else:
                sumc5 = ""

            if request.POST.get('mat_idc'):
                mat_idc = request.POST.get('mat_idc')
            if request.POST.get('matc0'):
                matc0 = request.POST.get('matc0')
            else:
                matc0 = ""
            if request.POST.get('matc1'):
                matc1 = request.POST.get('matc1')
            else:
                matc1 = ""
            if request.POST.get('matc2'):
                matc2 = request.POST.get('matc2')
            else:
                matc2 = ""
            if request.POST.get('matc3'):
                matc3 = request.POST.get('matc3')
            else:
                matc3 = ""

            if request.POST.get('fillup_idd[0]'):
                fillup_idd0 = request.POST.get('fillup_idd[0]')
            if request.POST.get('fillupd[0]'):
                fillupd0 = request.POST.get('fillupd[0]')
            if request.POST.get('fillup_idd[1]'):
                fillup_idd1 = request.POST.get('fillup_idd[1]')
            if request.POST.get('fillupd[1]'):
                fillupd1 = request.POST.get('fillupd[1]')
            if request.POST.get('fillup_idd[2]'):
                fillup_idd2 = request.POST.get('fillup_idd[2]')
            if request.POST.get('fillupd[2]'):
                fillupd2 = request.POST.get('fillupd[2]')

            if request.POST.get('mcqd[0]'):
                mcq_idd = request.POST.get('mcqd[0]')
            if request.POST.get('mcqqd[0]'):
                mcqd0 = request.POST.get('mcqqd[0]')

            if request.POST.get('mapd[0]'):
                map_idd0 = request.POST.get('mapd[0]')
            if request.POST.get('mappd[0]'):
                mapd0 = request.POST.get('mappd[0]')
            if request.POST.get('mapd[1]'):
                map_idd1 = request.POST.get('mapd[1]')
            if request.POST.get('mappd[1]'):
                mapd1 = request.POST.get('mappd[1]')
            if request.POST.get('mapd[2]'):
                map_idd2 = request.POST.get('mapd[2]')
            if request.POST.get('mappd[2]'):
                mapd2 = request.POST.get('mappd[2]')


            if request.POST.get('sumd'):
                sum_idd = request.POST.get('sumd')
            if request.POST.get('sumd0'):
                sumd0 = request.POST.get('sumd0')
            if request.POST.get('sumd1'):
                sumd1 = request.POST.get('sumd1')
            if request.POST.get('sumd2'):
                sumd2 = request.POST.get('sumd2')
            if request.POST.get('sumd3'):
                sumd3 = request.POST.get('sumd3')
            if request.POST.get('sumd4'):
                sumd4 = request.POST.get('sumd4')
            if request.POST.get('sumd5'):
                sumd5 = request.POST.get('sumd5')
            else:
                sumd5 = ""

            if request.POST.get('mat_idc'):
                mat_idd = request.POST.get('mat_idd')
            if request.POST.get('matd0'):
                matd0 = request.POST.get('matd0')
            else:
                matd0 = ""
            if request.POST.get('matd1'):
                matd1 = request.POST.get('matd1')
            else:
                matd1 = ""
            if request.POST.get('matd2'):
                matd2 = request.POST.get('matd2')
            else:
                matd2 = ""
            if request.POST.get('matd3'):
                matd3 = request.POST.get('matd3')
            else:
                matd3 = ""

        ListeningAnswer.objects.create(student=student, test_name=test_name,
                                     map_id0=map_id0, map0=map0, map_id1=map_id1, map1=map1,
                                     map_id2=map_id2, map2=map2,
                                     sum_id=sum_id, sum0=sum0, sum1=sum1, sum2=sum2, sum3=sum3, sum4=sum4, sum5=sum5,
                                     mcq_id=mcq_id, mcq0=mcq0,
                                     fillup_id0=fillup_id0, fillup_id1=fillup_id1, fillup_id2=fillup_id2,
                                     fillup0=fillup0, fillup1=fillup1, fillup2=fillup2, fillup_id3=fillup_id3, fillup3=fillup3,
                                     mat_id=mat_id, mat0=mat0, mat1=mat1, mat2=mat2,

                                     map_idb0=map_idb0, mapb0=mapb0, map_idb1=map_idb1, mapb1=mapb1,
                                     map_idb2=map_idb2, mapb2=mapb2,
                                     fillup_idb0=fillup_idb0, fillup_idb1=fillup_idb1, fillup_idb2=fillup_idb2,
                                     fillupb0=fillupb0, fillupb1=fillupb1, fillupb2=fillupb2,
                                     sum_idb=sum_idb, sumb0=sumb0, sumb1=sumb1, sumb2=sumb2, sumb3=sumb3,
                                     sumb4=sumb4, sumb5=sumb5,
                                     mat_idb=mat_idb, matb0=matb0, matb1=matb1, matb2=matb2, matb3=matb3,
                                     mcq_idb=mcq_idb, mcqb0=mcqb0,

                                     map_idc0=map_idc0, mapc0=mapc0, map_idc1=map_idc1, mapc1=mapc1,
                                     map_idc2=map_idc2, mapc2=mapc2,
                                     fillup_idc0=fillup_idc0, fillup_idc1=fillup_idc1, fillup_idc2=fillup_idc2,
                                     fillupc0=fillupc0, fillupc1=fillupc1, fillupc2=fillupc2,
                                     mat_idc=mat_idc, matc0=matc0, matc1=matc1, matc2=matc2, matc3=matc3,
                                     sum_idc=sum_idc, sumc0=sumc0, sumc1=sumc1, sumc2=sumc2, sumc3=sumc3,
                                     sumc4=sumc4, sumc5=sumc5,
                                     mcq_idc=mcq_idc, mcqc0=mcqc0,

                                     map_idd0=map_idd0, mapd0=mapd0, map_idd1=map_idd1, mapd1=mapd1,
                                     map_idd2=map_idd2, mapd2=mapd2,
                                     fillup_idd0=fillup_idd0, fillup_idd1=fillup_idd1, fillup_idd2=fillup_idd2,
                                     fillupd0=fillupd0, fillupd1=fillupd1, fillupd2=fillupd2,
                                     mat_idd=mat_idd, matd0=matd0, matd1=matd1, matd2=matd2, matd3=matd3,
                                     sum_idd=sum_idd, sumd0=sumd0, sumd1=sumd1, sumd2=sumd2, sumd3=sumd3,
                                     sumd4=sumd4, sumd5=sumd5,
                                     mcq_idd=mcq_idd, mcqd0=mcqd0,
                                     )
        return HttpResponse("<h4>aubmitted your test</h4>")
    else:
        usr = Assign.objects.filter(Student=request.user)
        test = "Listening Test "+part_id
        count = 0
        for i in usr:
            if i.test_name == test:
                count = 1
                audio = ListeningTest.objects.filter(id=part_id)
                mcq = MCQl.objects.all()
                mcqques = MCQQuesl.objects.all()
                summary = Summaryl.objects.all()
                fillup = Fillupl.objects.all()
                fillupques = FillupQuel.objects.all()
                matching = Matchingl.objects.all()
                map = MapMatchl.objects.all()
                mapques = MapMatchQuesl.objects.all()
                args = {'audio': audio, 'mcq': mcq, 'mcqques': mcqques, 'map': map, 'mapques': mapques,
                        'summary': summary, 'fillup': fillup, 'fillupques': fillupques, 'matching': matching}
                return render(request, 'ListeningTest.html', args)

        if count == 0:
            return HttpResponse("<h1>you are not authurised to give this test ask. Ask your teacher to allot you the test</h1>")




def WritingPaper(request, part_id):
    if request.method == 'POST':
        student = User.objects.get(username=request.user)
        if request.POST.get('test_name'):
            test_name = request.POST.get('test_name')
            ques1_id = request.POST.get('ques1_id')
        if request.POST.get('ans1'):
            ans1 = request.POST.get('ans1')
            ques2_id = request.POST.get('ques2_id')
        if request.POST.get('ans2'):
            ans2 = request.POST.get('ans2')
        WritingAnswer.objects.create(test_name=test_name, student=student, ques1=ques1_id, ans1=ans1, ques2=ques2_id, ans2=ans2)
        return HttpResponse("<h4>Submitted your test</h4>")
    else:
        usr = Assign.objects.filter(Student=request.user)
        test = "Writing Test 1"
        count = 0
        for i in usr :
            if i.test_name == test:
                count = 1
                writing = WritingTest.objects.filter(id=part_id)
                write = Writing.objects.all()
                args = {'write':write, 'writing':writing}
                return render(request, 'WritingTest.html', args)
        if count == 0:
            return HttpResponse("<h1>you are not authurised to give this test ask. Ask your teacher to allot you the test</h1>")



def Rinstruction(request):
    return render(request, 'rtest_inst.html')

def Winstruction(request):
    return render(request, 'wtest_inst.html')

def Linstruction(request):
    return render(request, 'ltest_inst.html')
