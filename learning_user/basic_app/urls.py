from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('register',views.form,name='register'),
    path('login',views.user_login,name='login_page'),
]

