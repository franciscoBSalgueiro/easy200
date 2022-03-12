from django.urls import path

from . import views

urlpatterns = [
    path('<int:user_id>/home', views.home, name='home'),
    path('login', views.login, name='login'),
    path('<int:user_id>/extrato', views.extrato, name='extrato')
]