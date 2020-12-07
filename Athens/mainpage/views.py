from django.shortcuts import render, redirect
from django.http import HttpResponse
from admin.models import *
import json, os
from django.core.paginator import Paginator
from os.path import basename
from django.views import View
from django.http import JsonResponse


class CreateView(View):
    def post(self, request):
        data = json.loads(request.body)
        customer_tbl(
            user_id = data['c_id'],
            user_pw = data['c_pw'],
        )

        if customer_tbl.objects.filter(user_id=data['c_id']).exists() == True:
            return JsonResponse({"message": "이미 존재하는 아이디입니다."}, status=401)

        else:
            customer_tbl.objects.create(user_id=data['c_id'], user_pw=data['c_pw'])
            return JsonResponse({"message": "회원으로 가입되셨습니다."}, status=200)
    def get(self, request):
        users = customer_tbl.object.values()
        return JsonResponse({"data" : list(users)}, status = 200)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        customer_tbl(
            user_id=data['c_id'],
            user_pw=data['c_pw'],
        )
        if customer_tbl.objects.filter(user_id=data['c_id'], user_pw=data['c_pw']).exists() == True:
            return JsonResponse({"message": "로그인에 성공하셨습니다."}, status=200)
        else:
            return JsonResponse({"message": "아이디나 비밀번호가 일치하지 않습니다."}, status=401)

    def get(self, request):
        user = customer_tbl.objects.values()
        return JsonResponse({"list": list(user)}, status=200)

#메인페이지 비로그인 상태 보이기
def mainpage(request):
    teacher_list = teacher_tbl.objects.all()
    lecture_list = lecture_tbl.objects.all()

    # 한명의 객체 뽑을 때
    # teacher = teacher_tbl.objects.get(t_no = 13)

    context = {'teacher_list': teacher_list, 'lecture_list': lecture_list}

    return render(request, 'mainpage/introduce.html', context)


############ 동현

def faq_list(request):
    faqlist = faq_tbl.objects.all()

    context = { 'faq_list' : faqlist }

    return render(request, 'mainpage/FrequentlyAskedQuestions.html', context)

def teacher_list(request):
    teacher_list = teacher_tbl.objects.all()
    lecture_list = lecture_tbl.objects.all()

    # 한명의 객체 뽑을 때
    # teacher = teacher_tbl.objects.get(t_no = 13)

    context = { 'teacher_list' : teacher_list, 'lecture_list' : lecture_list}

    return render(request, 'mainpage/introduce.html', context)

def notice_list(request):

    # 공지 구분이 전체인 경우만 출력하기 위해 filter를 걸어준다.
    notice_list = notice_tbl.objects.filter(notice_target = '전체')

    context = { 'notice_list' : notice_list }

    return render(request, 'mainpage/notice.html', context)

def notice_list2(request, notice_no):
    notice_list2 = notice_tbl.objects.get(notice_no = notice_no)

    context = { 'notice_list2' : notice_list2 }

    return render(request, 'mainpage/notice2.html', context)

def lecture_list(request):

    lecture_list = lecture_tbl.objects.all()

    context = { 'lecture_list' : lecture_list }

    return render(request, 'mainpage/lecture.html', context)

def Recruitment(request):
    return render(request, 'mainpage/Recruitment.html')

#온라인 자료
def mainpage_select_lecture(request):
    user_id = request.user
    customer_info = customer_tbl.objects.get(user_id = user_id)
    customer_no = customer_info.c_no
    training_info = training_tbl.objects.filter(c_no_id=customer_no)

    training_list = []

    for i in training_info:
        training_list.append(i)

    lec_no = []
    for i in range(len(training_list)):
        lec_no.append(training_list[i].l_no_id)

    teacherlist = []
    for i in lec_no:
        teacher_no = lecture_tbl.objects.get(l_no=i).t_no_id
        teacherlist.append(teacher_tbl.objects.get(t_no=teacher_no))

    lecturelist = []
    print(teacherlist)
    for i in range(len(teacherlist)):
        lec = lecture_tbl.objects.get(t_no_id=teacherlist[i].t_no)
        print(lec)
        lecturelist.append(lec)

    print(lecturelist)

    # teacher = teacher_tbl.objects.get(user=request.user.id)
    # lecture = lecture_tbl.objects.filter(t_no_id=teacher.t_no)
    context = {'customer_info': customer_info, 'lecturelist': lecturelist}
    return render(request, 'online/mainpage_select_lecture.html', context)

#온라인 자료 강의 선택
def mainpage_select_lecture(request):
    user_id = request.user
    customer_info = customer_tbl.objects.get(user_id = user_id)
    customer_no = customer_info.c_no
    training_info = training_tbl.objects.filter(c_no_id=customer_no)

    training_list = []

    for i in training_info:
        training_list.append(i.l_no_id)

    #강의 목록
    lec_list = []
    for i in training_list:
        lec_list.append(lecture_tbl.objects.get(l_no=i))

    context = { 'customer_info': customer_info, 'lec_list':lec_list}
    return render(request, 'online/mainpage_select_lecture.html', context)

#온라인 자료
def mainpage_select_online_index_teacher(request,pk):

    lecture = lecture_tbl.objects.get(l_no=pk)
    online= online_tbl.objects.filter(l_no_id=lecture.l_no).order_by('-on_date')
    # 페이징
    page = request.GET.get('page', '1')  # 페이지
    paginator = Paginator(online, 10)  # 페이지당 10개
    page_obj = paginator.get_page(page)
    context = {'online': page_obj}

    return render(request, 'online/mainpage_select_teacher.html', context)


def mainpage_online_contents(request,pk):
    content = online_tbl.objects.get(pk=pk)
    fname=''
    fsize=0
    if content.on_file:
        file = content.on_file
        fname= basename(file.name)
        try:
            with open('%s'%(fname),'wb') as fp:
                for chunk in file.chunks():
                    fp.write(chunk)
            fsize=round(os.path.getsize(fname)/1024)
        except:
            pass
    context={'content':content,'fname':fname,'fsize':fsize}
    return render(request, 'online/mainpage_online_contents.html', context)
# Create your views here.

