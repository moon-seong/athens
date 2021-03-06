from django.http import HttpResponse
from django.shortcuts import render
from admin.models import *
from .forms import timeform
from django.utils import timezone
from datetime import datetime
# Create your views here.

def select_lecture_teacher(request):
    teacher = teacher_tbl.objects.get(user=request.user.id)
    lecture =lecture_tbl.objects.filter(t_no_id=teacher.t_no)
    context = {'lecture':lecture}
    return render(request, 'manage/select_lecture.html', context)

def student_info_manage(request,pk):

    # 학생정보
    lecture = lecture_tbl.objects.get(pk=pk)
    training = training_tbl.objects.filter(l_no=pk)
    student_list = []
    try:
        for i in range(len(training)):
            student_info = training[i]
            student_list.append(student_info)
    except:
        pass

    # 성적관리
    test = test_tbl.objects.filter(l_no=lecture.l_no).order_by('-te_join')
    test_list = []
    try:
        for i in range(len(test)):
            test_info = test[i]
            test_list.append(test_info)
    except:
        pass

    # 출결
    form = timeform()
    error= False
    set_attendance= False
    student_attendance = []
    atd_list= []
    date=''
    if request.method == "POST":
        if request.POST['button'] == '1':
            if request.POST['at_date'] <= datetime.today().strftime("%Y-%m-%d"):
                form.save(commit=False)
                set_attendance = True
                date= request.POST['at_date']
                try:
                    for i in range(len(training)):
                        student_name = training[i]
                        if student_name.tr_date.strftime("%Y-%m-%d") <= request.POST['at_date']:
                            student_attendance.append(student_name)
                            try:
                                atd= attendance_tbl.objects.get(tr_no_id=student_name.tr_no,at_date=request.POST['at_date'])
                                atd_list.append(atd.attendance)
                            except:
                                pass
                except:
                    pass
            else:
                error = True


        if request.POST['button'] == '2':
            for i in range(len(training)):
                try:
                    save_atd=attendance_tbl.objects.get(tr_no_id=request.POST['%s'%(training[i].tr_no)],at_date=request.POST['date'])

                    save_atd.attendance = request.POST['atd%s'%(training[i].tr_no)]

                    save_atd.at_date = request.POST['date']
                    save_atd.save()
                except:
                    attendance_tbl.objects.create(tr_no_id=request.POST['%s'%(training[i].tr_no)],attendance=request.POST['atd%s'%(training[i].tr_no)],at_date=request.POST['date'])
            return HttpResponse('<script type="text/javascript"> alert("출석부가 저장되었습니다."); history.back();</script>')

        context = {'lecture': lecture, 'training': training, 'student_list': student_list, 'form': form, 'error': error,
                   'set_attendance': set_attendance, 'student_attendance': student_attendance, 'date': date,
                   'atd_list': atd_list, 'test_list': test_list,'pass':1}
        return render(request, 'manage/lecture_manage.html', context)

    context = {'lecture':lecture, 'training': training, 'student_list': student_list,'form':form,'error':error,'set_attendance':set_attendance,'student_attendance':student_attendance,'date':date,'atd_list':atd_list,'test_list':test_list}
    return render(request, 'manage/lecture_manage.html', context)

def look_up_score(request,pk):
    test = test_tbl.objects.get(pk=pk)
    test_score = test_apply.objects.filter(te_no=pk).order_by('-te_score')
    score_list=[]
    try:
        for i in range(len(test_score)):
            test_info = test_score[i]
            score_list.append(test_info)
    except:
        pass
    context = {'test':test,'score_list':score_list}
    return render(request,'manage/look_up_score.html',context)