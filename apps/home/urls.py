from django.urls import path, include
from .import views

# from apps.coursar.views import cours_ar
# from apps.coursfr.views import cours_fr
urlpatterns = [
    path('', views.home, name="home"),
    path('courses/', views.courses, name="courses"),
    # path('load/', views.load, name="load"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    # path('brevet-ar/2020/<slug:slug>/', views.b_ar_d_20,name='b_detail-20'),
    
    path('Arabic-cours/', include('apps.coursar.urls'), name='cours_ar'),
    path('French-cours/', include('apps.coursfr.urls'), name='cours_fr'),

]