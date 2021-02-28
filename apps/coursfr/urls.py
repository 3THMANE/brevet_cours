from django.urls import path
from .import views

urlpatterns = [
    path('courses/fr/', views.coursesfr, name="coursesfr"),
    path('brevet-fr/2020/', views.b_fr_20,name='b_fr_20'),
    path('brevet-fr/2019/', views.b_fr_19,name='b_fr_19'),
    path('brevet-fr/2018/', views.b_fr_18,name='b_fr_18'),
    path('brevet-fr/2017/', views.b_fr_17,name='b_fr_17'),
    path('brevet-fr/2016/', views.b_fr_16,name='b_fr_16'),
    path('brevet-fr/2015/', views.b_fr_15,name='b_fr_15'),
    
    
    path('coursesfr/<slug>', views.c_f_detail, name="detail"),
    path('brevet-fr/2020/<slug:slug>', views.b_fr_d_20,name='f_detail_20'),
    path('brevet-fr/2019/<slug:slug>', views.b_fr_d_19,name='f_detail_19'),
    path('brevet-fr/2018/<slug:slug>', views.b_fr_d_18,name='f_detail_18'),
    path('brevet-fr/2017/<slug:slug>', views.b_fr_d_17,name='f_detail_17'),
    path('brevet-fr/2016/<slug:slug>', views.b_fr_d_16,name='f_detail_16'),
    path('brevet-fr/2015/<slug:slug>', views.b_fr_d_15,name='f_detail_15'),
    
]
