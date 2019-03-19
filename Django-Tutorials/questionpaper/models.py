from django.db import models
from reading.models import passageMain
from listening.models import AudioMain
from writing.models import Writing
# Create your models here.

class ReadingTest(models.Model):
    test_name = models.CharField(max_length=100, default="Reading Test")
    ques1 = models.ForeignKey(passageMain, related_name="Reading1", on_delete=models.PROTECT)
    ques2 = models.ForeignKey(passageMain, related_name="Reading2", on_delete=models.PROTECT)
    ques3 = models.ForeignKey(passageMain, related_name="Reading3", on_delete=models.PROTECT)

    def __str__(self):
        return self.test_name

class ListeningTest(models.Model):
    test_name = models.CharField(max_length=100, default="Listening Test")
    ques1 = models.ForeignKey(AudioMain, related_name="Listening1", on_delete=models.PROTECT)
    ques2 = models.ForeignKey(AudioMain, related_name="Listening2", on_delete=models.PROTECT)
    ques3 = models.ForeignKey(AudioMain, related_name="Listening3", on_delete=models.PROTECT)
    ques4 = models.ForeignKey(AudioMain, related_name="Listening4", on_delete=models.PROTECT)

    def __str__(self):
        return  self.test_name


class WritingTest(models.Model):
    test_name = models.CharField(max_length=100, default="Writing Test")
    ques1 = models.ForeignKey(Writing, related_name="Listening1", on_delete=models.PROTECT)
    ques2 = models.ForeignKey(Writing, related_name="Listening2", on_delete=models.PROTECT)

    def __str__(self):
        return self.test_name



class WritingAnswer(models.Model):
    test_name = models.CharField(max_length=100, default="Writing Test")
    student = models.CharField(max_length=100, null=True)
    ques1 = models.TextField(max_length=100, null=True)
    ans1 = models.TextField(max_length=1000000, default="Nothing Wriiten by the Student")
    ques2 = models.TextField(max_length=100, null=True)
    ans2 = models.TextField(max_length=1000000, default="Nothing Wriiten by the Student")

    def __str__(self):
        return self.student



class ReadingAnswer(models.Model):
    test_name = models.CharField(max_length=100, default="Reading Test")
    student = models.CharField(max_length=100, null=True)
    ysn_ida0 = models.IntegerField(null=True)
    ysna0 = models.CharField(max_length=10, null=True)
    ysn_ida1 = models.IntegerField(null=True)
    ysna1 = models.CharField(max_length=10, null=True)
    ysn_ida2 = models.IntegerField(null=True)
    ysna2 = models.CharField(max_length=10, null=True)
    ysn_ida3 = models.IntegerField(null=True)
    ysna3 = models.CharField(max_length=10, null=True)
    ysn_ida4 = models.IntegerField(null=True)
    ysna4 = models.CharField(max_length=10, null=True)
    ysn_ida5 = models.IntegerField(null=True)
    ysna5 = models.CharField(max_length=10, null=True)

    sum_ida = models.IntegerField(null=True)
    suma0 = models.CharField(max_length=100, null=True)
    suma1 = models.CharField(max_length=100, null=True)
    suma2 = models.CharField(max_length=100, null=True)
    suma3 = models.CharField(max_length=100, null=True)
    suma4 = models.CharField(max_length=100, null=True)
    suma5 = models.CharField(max_length=100, null=True)

    mcq_ida = models.IntegerField(null=True)
    mcqa0 = models.CharField(max_length=100, null=True)

    fillup_ida0 = models.IntegerField(null=True)
    fillupa0 = models.CharField(max_length=100, null=True)
    fillup_ida1 = models.IntegerField(null=True)
    fillupa1 = models.CharField(max_length=100, null=True)
    fillup_ida2 = models.IntegerField(null=True)
    fillupa2 = models.CharField(max_length=100, null=True)

    mat_ida = models.IntegerField(null=True)
    mata0 = models.CharField(max_length=10, null=True)
    mata1 = models.CharField(max_length=10, null=True)
    mata2 = models.CharField(max_length=10, null=True)
    mata3 = models.CharField(max_length=10, null=True)
    mata4 = models.CharField(max_length=10, null=True)
    mata5 = models.CharField(max_length=10, null=True)

    ysn_idb0 = models.IntegerField(null=True)
    ysnb0 = models.CharField(max_length=10, null=True)
    ysn_idb1 = models.IntegerField(null=True)
    ysnb1 = models.CharField(max_length=10, null=True)
    ysn_idb2 = models.IntegerField(null=True)
    ysnb2 = models.CharField(max_length=10, null=True)
    ysn_idb3 = models.IntegerField(null=True)
    ysnb3 = models.CharField(max_length=10, null=True)
    ysn_idb4 = models.IntegerField(null=True)
    ysnb4 = models.CharField(max_length=10, null=True)
    ysn_idb5 = models.IntegerField(null=True)
    ysnb5 = models.CharField(max_length=10, null=True)

    sum_idb = models.IntegerField(null=True)
    sumb0 = models.CharField(max_length=100, null=True)
    sumb1 = models.CharField(max_length=100, null=True)
    sumb2 = models.CharField(max_length=100, null=True)
    sumb3 = models.CharField(max_length=100, null=True)
    sumb4 = models.CharField(max_length=100, null=True)
    sumb5 = models.CharField(max_length=100, null=True)

    mcq_idb = models.IntegerField(null=True)
    mcqb0 = models.CharField(max_length=100, null=True)

    fillup_idb0 = models.IntegerField(null=True)
    fillupb0 = models.CharField(max_length=100, null=True)
    fillup_idb1 = models.IntegerField(null=True)
    fillupb1 = models.CharField(max_length=100, null=True)
    fillup_idb2 = models.IntegerField(null=True)
    fillupb2 = models.CharField(max_length=100, null=True)

    mat_idb = models.IntegerField(null=True)
    matb0 = models.CharField(max_length=10, null=True)
    matb1 = models.CharField(max_length=10, null=True)
    matb2 = models.CharField(max_length=10, null=True)
    matb3 = models.CharField(max_length=10, null=True)
    matb4 = models.CharField(max_length=10, null=True)
    matb5 = models.CharField(max_length=10, null=True)

    ysn_idc0 = models.IntegerField(null=True)
    ysnc0 = models.CharField(max_length=10, null=True)
    ysn_idc1 = models.IntegerField(null=True)
    ysnc1 = models.CharField(max_length=10, null=True)
    ysn_idc2 = models.IntegerField(null=True)
    ysnc2 = models.CharField(max_length=10, null=True)
    ysn_idc3 = models.IntegerField(null=True)
    ysnc3 = models.CharField(max_length=10, null=True)
    ysn_idc4 = models.IntegerField(null=True)
    ysnc4 = models.CharField(max_length=10, null=True)
    ysn_idc5 = models.IntegerField(null=True)
    ysnc5 = models.CharField(max_length=10, null=True)

    sum_idc = models.IntegerField(null=True)
    sumc0 = models.CharField(max_length=100, null=True)
    sumc1 = models.CharField(max_length=100, null=True)
    sumc2 = models.CharField(max_length=100, null=True)
    sumc3 = models.CharField(max_length=100, null=True)
    sumc4 = models.CharField(max_length=100, null=True)
    sumc5 = models.CharField(max_length=100, null=True)

    mcq_idc = models.IntegerField(null=True)
    mcqc0 = models.CharField(max_length=100, null=True)

    fillup_idc0 = models.IntegerField(null=True)
    fillupc0 = models.CharField(max_length=100, null=True)
    fillup_idc1 = models.IntegerField(null=True)
    fillupc1 = models.CharField(max_length=100, null=True)
    fillup_idc2 = models.IntegerField(null=True)
    fillupc2 = models.CharField(max_length=100, null=True)

    mat_idc = models.IntegerField(null=True)
    matc0 = models.CharField(max_length=10, null=True)
    matc1 = models.CharField(max_length=10, null=True)
    matc2 = models.CharField(max_length=10, null=True)
    matc3 = models.CharField(max_length=10, null=True)
    matc4 = models.CharField(max_length=10, null=True)
    matc5 = models.CharField(max_length=10, null=True)

    ysn_idd0 = models.IntegerField(null=True)
    ysnd0 = models.CharField(max_length=10, null=True)
    ysn_idd1 = models.IntegerField(null=True)
    ysnd1 = models.CharField(max_length=10, null=True)
    ysn_idd2 = models.IntegerField(null=True)
    ysnd2 = models.CharField(max_length=10, null=True)
    ysn_idd3 = models.IntegerField(null=True)
    ysnd3 = models.CharField(max_length=10, null=True)
    ysn_idd4 = models.IntegerField(null=True)
    ysnd4 = models.CharField(max_length=10, null=True)
    ysn_idd5 = models.IntegerField(null=True)
    ysnd5 = models.CharField(max_length=10, null=True)

    sum_idd = models.IntegerField(null=True)
    sumd0 = models.CharField(max_length=100, null=True)
    sumd1 = models.CharField(max_length=100, null=True)
    sumd2 = models.CharField(max_length=100, null=True)
    sumd3 = models.CharField(max_length=100, null=True)
    sumd4 = models.CharField(max_length=100, null=True)
    sumd5 = models.CharField(max_length=100, null=True)

    mcq_idd = models.IntegerField(null=True)
    mcqd0 = models.CharField(max_length=100, null=True)

    fillup_idd0 = models.IntegerField(null=True)
    fillupd0 = models.CharField(max_length=100, null=True)
    fillup_idd1 = models.IntegerField(null=True)
    fillupd1 = models.CharField(max_length=100, null=True)
    fillup_idd2 = models.IntegerField(null=True)
    fillupd2 = models.CharField(max_length=100, null=True)

    mat_idd = models.IntegerField(null=True)
    matd0 = models.CharField(max_length=10, null=True)
    matd1 = models.CharField(max_length=10, null=True)
    matd2 = models.CharField(max_length=10, null=True)
    matd3 = models.CharField(max_length=10, null=True)
    matd4 = models.CharField(max_length=10, null=True)
    matd5 = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.test_name



class ListeningAnswer(models.Model):
    test_name = models.CharField(max_length=100, default="Reading Test")
    student = models.CharField(max_length=100, null=True)
    map_id0 = models.IntegerField(null=True)
    map0 = models.CharField(max_length=10, null=True)
    map_id1 = models.IntegerField(null=True)
    map1 = models.CharField(max_length=10, null=True)
    map_id2 = models.IntegerField(null=True)
    map2 = models.CharField(max_length=10, null=True)
    map_id3 = models.IntegerField(null=True)
    map3 = models.CharField(max_length=10, null=True)
    map_id4 = models.IntegerField(null=True)
    map4 = models.CharField(max_length=10, null=True)
    map_id5 = models.IntegerField(null=True)
    map5 = models.CharField(max_length=10, null=True)

    sum_id = models.IntegerField(null=True)
    sum0 = models.CharField(max_length=100, null=True)
    sum1 = models.CharField(max_length=100, null=True)
    sum2 = models.CharField(max_length=100, null=True)
    sum3 = models.CharField(max_length=100, null=True)
    sum4 = models.CharField(max_length=100, null=True)
    sum5 = models.CharField(max_length=100, null=True)

    mcq_id = models.IntegerField(null=True)
    mcq0 = models.CharField(max_length=100, null=True)

    fillup_id0 = models.IntegerField(null=True)
    fillup0 = models.CharField(max_length=100, null=True)
    fillup_id1 = models.IntegerField(null=True)
    fillup1 = models.CharField(max_length=100, null=True)
    fillup_id2 = models.IntegerField(null=True)
    fillup2 = models.CharField(max_length=100, null=True)
    fillup_id3 = models.IntegerField(null=True)
    fillup3 = models.CharField(max_length=100, null=True)

    mat_id = models.IntegerField(null=True)
    mat0 = models.CharField(max_length=10, null=True)
    mat1 = models.CharField(max_length=10, null=True)
    mat2 = models.CharField(max_length=10, null=True)
    mat3 = models.CharField(max_length=10, null=True)
    mat4 = models.CharField(max_length=10, null=True)
    mat5 = models.CharField(max_length=10, null=True)

    map_idb0 = models.IntegerField(null=True)
    mapb0 = models.CharField(max_length=10, null=True)
    map_idb1 = models.IntegerField(null=True)
    mapb1 = models.CharField(max_length=10, null=True)
    map_idb2 = models.IntegerField(null=True)
    mapb2 = models.CharField(max_length=10, null=True)
    map_idb3 = models.IntegerField(null=True)
    mapb3 = models.CharField(max_length=10, null=True)
    map_idb4 = models.IntegerField(null=True)
    mapb4 = models.CharField(max_length=10, null=True)
    map_idb5 = models.IntegerField(null=True)
    mapb5 = models.CharField(max_length=10, null=True)

    sum_idb = models.IntegerField(null=True)
    sumb0 = models.CharField(max_length=100, null=True)
    sumb1 = models.CharField(max_length=100, null=True)
    sumb2 = models.CharField(max_length=100, null=True)
    sumb3 = models.CharField(max_length=100, null=True)
    sumb4 = models.CharField(max_length=100, null=True)
    sumb5 = models.CharField(max_length=100, null=True)

    mcq_idb = models.IntegerField(null=True)
    mcqb0 = models.CharField(max_length=100, null=True)

    fillup_idb0 = models.IntegerField(null=True)
    fillupb0 = models.CharField(max_length=100, null=True)
    fillup_idb1 = models.IntegerField(null=True)
    fillupb1 = models.CharField(max_length=100, null=True)
    fillup_idb2 = models.IntegerField(null=True)
    fillupb2 = models.CharField(max_length=100, null=True)

    mat_idb = models.IntegerField(null=True)
    matb0 = models.CharField(max_length=10, null=True)
    matb1 = models.CharField(max_length=10, null=True)
    matb2 = models.CharField(max_length=10, null=True)
    matb3 = models.CharField(max_length=10, null=True)
    matb4 = models.CharField(max_length=10, null=True)
    matb5 = models.CharField(max_length=10, null=True)

    map_idc0 = models.IntegerField(null=True)
    mapc0 = models.CharField(max_length=10, null=True)
    map_idc1 = models.IntegerField(null=True)
    mapc1 = models.CharField(max_length=10, null=True)
    map_idc2 = models.IntegerField(null=True)
    mapc2 = models.CharField(max_length=10, null=True)
    map_idc3 = models.IntegerField(null=True)
    mapc3 = models.CharField(max_length=10, null=True)
    map_idc4 = models.IntegerField(null=True)
    mapc4 = models.CharField(max_length=10, null=True)
    map_idc5 = models.IntegerField(null=True)
    mapc5 = models.CharField(max_length=10, null=True)

    sum_idc = models.IntegerField(null=True)
    sumc0 = models.CharField(max_length=100, null=True)
    sumc1 = models.CharField(max_length=100, null=True)
    sumc2 = models.CharField(max_length=100, null=True)
    sumc3 = models.CharField(max_length=100, null=True)
    sumc4 = models.CharField(max_length=100, null=True)
    sumc5 = models.CharField(max_length=100, null=True)

    mcq_idc = models.IntegerField(null=True)
    mcqc0 = models.CharField(max_length=100, null=True)

    fillup_idc0 = models.IntegerField(null=True)
    fillupc0 = models.CharField(max_length=100, null=True)
    fillup_idc1 = models.IntegerField(null=True)
    fillupc1 = models.CharField(max_length=100, null=True)
    fillup_idc2 = models.IntegerField(null=True)
    fillupc2 = models.CharField(max_length=100, null=True)

    mat_idc = models.IntegerField(null=True)
    matc0 = models.CharField(max_length=10, null=True)
    matc1 = models.CharField(max_length=10, null=True)
    matc2 = models.CharField(max_length=10, null=True)
    matc3 = models.CharField(max_length=10, null=True)
    matc4 = models.CharField(max_length=10, null=True)
    matc5 = models.CharField(max_length=10, null=True)

    map_idd0 = models.IntegerField(null=True)
    mapd0 = models.CharField(max_length=10, null=True)
    map_idd1 = models.IntegerField(null=True)
    mapd1 = models.CharField(max_length=10, null=True)
    map_idd2 = models.IntegerField(null=True)
    mapd2 = models.CharField(max_length=10, null=True)
    map_idd3 = models.IntegerField(null=True)
    mapd3 = models.CharField(max_length=10, null=True)
    map_idd4 = models.IntegerField(null=True)
    mapd4 = models.CharField(max_length=10, null=True)
    map_idd5 = models.IntegerField(null=True)
    mapd5 = models.CharField(max_length=10, null=True)

    sum_idd = models.IntegerField(null=True)
    sumd0 = models.CharField(max_length=100, null=True)
    sumd1 = models.CharField(max_length=100, null=True)
    sumd2 = models.CharField(max_length=100, null=True)
    sumd3 = models.CharField(max_length=100, null=True)
    sumd4 = models.CharField(max_length=100, null=True)
    sumd5 = models.CharField(max_length=100, null=True)

    mcq_idd = models.IntegerField(null=True)
    mcqd0 = models.CharField(max_length=100, null=True)

    fillup_idd0 = models.IntegerField(null=True)
    fillupd0 = models.CharField(max_length=100, null=True)
    fillup_idd1 = models.IntegerField(null=True)
    fillupd1 = models.CharField(max_length=100, null=True)
    fillup_idd2 = models.IntegerField(null=True)
    fillupd2 = models.CharField(max_length=100, null=True)

    mat_idd = models.IntegerField(null=True)
    matd0 = models.CharField(max_length=10, null=True)
    matd1 = models.CharField(max_length=10, null=True)
    matd2 = models.CharField(max_length=10, null=True)
    matd3 = models.CharField(max_length=10, null=True)
    matd4 = models.CharField(max_length=10, null=True)
    matd5 = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.test_name

