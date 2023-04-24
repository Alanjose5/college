from django.urls import path
from . import views
urlpatterns=[
    path('', views.demo, name="demo"),
    path('log',views.login,name="log"),
    path('register',views.register,name="register"),
    path('bio',views.detail,name="bio"),
    path('logout',views.logout,name="logout")
]