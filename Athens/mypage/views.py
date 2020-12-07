from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from admin.models import *
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
#스케줄러

#마이페이지 Default 페이지, 개인정보 수정 페이지
def mypage(request):
    user_no = request.user.id
    customer_info = customer_tbl.objects.get(user_id=user_no)  # 사용자 정보 가져오기
    contexts = {'customer_info': customer_info}
    if request.method == "POST":
        # 로그인 한 유저의 객체를 가져온다.
        user_info = request.user
        if request.POST['btn'] == '확인':
            username = user_info.username
            password = request.POST['passwd']  # 입력한 비밀번호
            user = authenticate(username = username, password = password)
            context = {'user_info': user_info, 'customer_info' : customer_info}

            if user is not None:
                #개인정보 수정페이지로...
                return render(request, 'mypage/information_insert.html', context)

        elif request.POST['btn'] == '저장':
            customer_info.c_phone = request.POST['userphone']
            context = {'user_info': user_info, 'customer_info': customer_info}
            if (request.POST['userphone'] != " "):
                customer_info.c_add = request.POST['useradd']
                customer_info.save()
            else:
                return render(request, 'mypage/information_insert.html', contexts)  # 템플릿 파일 경로 지정
        else:
            return render(request, 'mypage/checkpw.html', contexts)

    return render(request, 'mypage/checkpw.html', contexts)



def mypagepw(request):
    user_id = request.user.id
    customer_info = customer_tbl.objects.get(user_id=user_id)
    contexts = {'customer_info': customer_info}

    if request.method == "POST":
        user = request.user
        input_pw = request.POST.get('passwd')

        if request.POST['btn'] == '확인':
            print('확인')
            current_name = user.username
            user = authenticate(username = current_name, password = input_pw)
            context = {'user_info' : user, 'customer_info' : customer_info}

            if user is not None:
                #개인정보 수정페이지로...
                return render(request, 'mypage/change_pw.html', context)

        elif request.POST['btn'] == "저장":
            print('저장')
            origin = request.POST.get('userpw')
            if check_password(origin, user.password):
                new_password = request.POST.get('newuserpw')
                password_confirm = request.POST.get('newuserpwcheck')
                if new_password == password_confirm:
                    user.set_password(new_password)
                    user.save()
                    logout(request)
                    return HttpResponse(
                        '<script type="text/javascript">alert("로그아웃 되었습니다. 다시 로그인 해주세요."); location.href  ="/main"; </script>')

                else:
                    HttpResponse(
                        '<script type="text/javascript">alert("오류입니다."); location.href  ="/my/pw"; </script>')

    return render(request, 'mypage/changepw_checkpage.html', contexts)

def mychlid(request):
    user_id = request.user.id
    child = {}
    #부모 정보
    customer_info = customer_tbl.objects.get(user_id=user_id)
    context = {'customer_info' : customer_info}
    #부모 코드
    pcode = customer_info.c_code_valid

    #자녀 코드 -- 부모코드 조인
    ccode = customer_tbl.objects.filter(c_code=pcode) # 4번

    #자녀 다수 일 경우
    childlist = []
    for i in ccode:
        childlist.append(i)

    total_list = []

    print(childlist)

    for i in range(len(childlist)):
        temp_list = []
        # 자녀 정보 -- 수강 # 자녀 코드와 같은 수강 번호
        lecno = training_tbl.objects.get(c_no_id=childlist[i]).l_no_id
        # # 강의 번호
        # lecno = tr_info.l_no_id
        # 강의 정보 출력
        lec_info = lecture_tbl.objects.get(l_no=lecno)
        print(lec_info)
        # 선생님 정보
        tea_no = lec_info.t_no_id
        teacher_info = teacher_tbl.objects.get(t_no=tea_no)

        temp_list.append(childlist[i])
        temp_list.append(lec_info)
        temp_list.append(teacher_info)

        total_list.append(temp_list)


    # 재원 중일 경우
    if childlist.c_state == 1:
        context = {'total_list': total_list,  'customer_info' : customer_info}
        return render(request, "mypage/child.html", context)

    #재원중이 아닐 경우
    else:
        return HttpResponse(
            '<script type="text/javascript">alert("재학생이 아닙니다."); location.href  ="/my"; </script>')

def myaddcode(request):
    #로그인한 부모 정보
    user_id = request.user.id
    customer_info= customer_tbl.objects.get(user_id=user_id)

    #부모 코드
    pcode = customer_info.c_code_valid
    #첫 번째 자녀 정보
    first_child = customer_tbl.objects.filter(c_code=pcode)
    childlist = []
    for i in first_child:
        childlist.append(i)
    first_child = childlist[0]
    contexts = {'customer_info': customer_info, 'first_child': first_child}
    #입력한 자녀 코드
    if request.method == 'POST':
        second_childcode = request.POST['changeusercode']

        second_child = customer_tbl.objects.get(c_code=second_childcode)
        second_child.c_code = first_child.c_code

        second_child.save()
        return render(request, 'mypage/checkpw.html', contexts)

    return render(request, 'mypage/addcode.html', contexts)

#결제 내역
def mypagefee(request):
    # 로그인한 부모 정보
    user_id = request.user.id
    customer_info = customer_tbl.objects.get(user_id=user_id)
    cust_no = customer_info.c_no

    trinfo = training_tbl.objects.filter(c_no_id=cust_no)

    lecture_list = []
    for i in range(len(trinfo)):
        lecno = trinfo[i].l_no_id
        lecture_info = lecture_tbl.objects.get(l_no=lecno)
        lecture_list.append(lecture_info)


    contexts = {'customer_info': customer_info, 'lecture_list':lecture_list}
    return render(request, 'mypage/fee.html', contexts)

def mypageattend(request):
    user_id = request.user.id
    customer_info = customer_tbl.objects.get(user_id=user_id)
    cust_no = customer_info.c_no

    trlist = training_tbl.objects.filter(c_no_id=cust_no)

    lecture_list = []
    for i in range(len(trlist)):
        lecno = trlist[i].l_no_id
        lecture_info = lecture_tbl.objects.get(l_no=lecno)
        lecture_list.append(lecture_info)

    attend = []

    for i in range(len(trlist)):
        training_no = trlist[i].tr_no
        attendlist = attendance_tbl.objects.filter(tr_no_id=training_no)
        attend.append(attendlist)

    contexts = {'customer_info': customer_info, 'attend': attend, 'lecture_list': lecture_list}
    return render(request, 'mypage/attendance.html', contexts)

# Create your views here.
