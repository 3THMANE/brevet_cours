from django.urls import path
from .import views

urlpatterns = [
    path('brevet-ar/2020/', views.b_ar_20, name='b_ar_20'),
    # path('b-ar', views.cours, name='cours'),(?P<slug>[-a-zA-Z0-9_]+)/$'
    # path('brevet-ar/2020/<slug:slug>/', views.b_ar_20,name='b_ar_20'),
    # path('brevet-ar/2020/', views.b_ar_20,name='b_a_detail_20'),
    path('brevet-ar/2019/', views.b_ar_19,name='b_ar_19'),
    path('brevet-ar/2018/', views.b_ar_18,name='b_ar_18'),
    path('brevet-ar/2017/', views.b_ar_17,name='b_ar_17'),
    path('brevet-ar/2016/', views.b_ar_16,name='b_ar_16'),
    path('brevet-ar/2015/', views.b_ar_15,name='b_ar_15'),
    
    
    
    path('brevet-ar/2020/<slug:slug>', views.b_ar_d_20,name='b_a_detail_20'),
    path('brevet-ar/2019/<slug:slug>', views.b_ar_d_19,name='b_a_detail_19'),
    path('brevet-ar/2018/<slug:slug>', views.b_ar_d_18,name='b_a_detail_18'),
    path('brevet-ar/2017/<slug:slug>', views.b_ar_d_17,name='b_a_detail_17'),
    path('brevet-ar/2016/<slug:slug>', views.b_ar_d_16,name='b_a_detail_16'),
    path('brevet-ar/2015/<slug:slug>', views.b_ar_d_15,name='b_a_detail_15'),
    
]
