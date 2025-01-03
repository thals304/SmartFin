from django.urls import path
from . import views  # 현재 디렉터리에 있는 views 파일 임포트

urlpatterns = [
    path('', views.index),  # 기본 경로에 대한 뷰 연결
]