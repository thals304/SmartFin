from django.urls import path

from . import views  # 현재 디렉터리에 있는 views 파일 임포트

urlpatterns = [
    path('', views.mainpage),
    path('company/', views.company),
]