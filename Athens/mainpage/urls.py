from django.urls import path
from mainpage import views


urlpatterns = [
    path('', views.mainpage),
    # 동현
    path('FrequentlyAskedQuestions/', views.faq_list, name = 'faq_list'),
    path('introduce/', views.teacher_list, name = 'teacher_list'),
    path('notice/', views.notice_list, name = 'notice_list'),
    path('notice2/<int:notice_no>', views.notice_list2, name = 'notice_list2'),
    path('lecture/', views.lecture_list, name='lecture_list'),
    path('Recruitment/', views.Recruitment),
    path('online/', views.mainpage_select_lecture),
    path('online/<int:pk>', views.mainpage_select_online_index_teacher),
    path('online/content/<int:pk>', views.mainpage_online_contents),
]

