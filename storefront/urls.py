from django.urls import  path
from . import views
from .views import DetailView

urlpatterns=[
    path('',views.homepage, name='homepage'),
    path('<int:pk>/', DetailView.as_view(), name='detailpage'),
    path('logout',views.logout, name='logout'),
    path('register/', views.register),
    path('login',views.signin), 
    path('register/login.html', views.homepage),
    path('register/create-account.html', views.register),
    path('register/register', views.register),
    path('homepage.html',views.homepage)
]

