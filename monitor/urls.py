from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('teacherView/', views.teacherView, name="teacherView"),
    path('studentView/<str:rollNumber>', views.studentView, name="studentView"),
]
