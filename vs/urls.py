from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'vs'
urlpatterns = [
    path('', views.indexview, name='index'),
    path("poll/",views.pollview,name='poll'),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('candidate/detail/<int:id>/', views.candidateDetailView, name='detail'),
    path('result/', views.resultView, name='result'),
    path("login/",views.loginView,name='login'),
    path("logout/",views.logoutview,name='logout'),
    path("register/",views.registrationview,name='register'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
