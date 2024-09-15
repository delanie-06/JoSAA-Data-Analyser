from main import views
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('',views.index,name="home"),
    path('predicator/', views.predicator_view, name='predicator'),
    path('analyse/', views.analyse_iit_view, name='analyse'),
    path('branch/', views.analyse_branch_view, name='branch'),
    path('branch_cut/', views.analyse_branch_cut_view, name='analyse_branch_cut'),
    path('institute_cut/', views.analyse_inst_cut_view, name='analyse_inst_cut'),
    path('iitwise/<str:inst>', views.iitwise_view, name='iitwise'),
    path('coursewise/<str:inst>', views.coursewise_view, name='coursewise'),


]
