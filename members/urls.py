from django.urls import path
from members import views

urlpatterns = [
    path('', views.show_ch, name='enter_staff'),
]
