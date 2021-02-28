from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from .models import Brevet_Ar
from .models import Cours_Ar

def coursesar(request):
    cours_ar = Cours_Ar.objects.order_by('-create')
   
    return render(request, 'ar/all_ar.html',{
        'cours_ar':cours_ar,
        
        })

def c_a_detail(request, slug):
    c_a_detail = Cours_Ar.objects.get(slug=slug)
    return render(request, 'home/all_d.html',{
        'c_a_detail':c_a_detail
        
        }) 

def b_ar_20(request):
    b_ar_20 = Brevet_Ar.objects.filter(select_brevet='brevet_ar_20')[0:4]
    return render(request,'ar/cours_ar.html',{'b_ar_20' : b_ar_20})
    
def b_ar_19(request):
    b_ar_19 = Brevet_Ar.objects.filter(select_brevet='brevet_ar_19')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_19':b_ar_19})

def b_ar_18(request):
    b_ar_18 = Brevet_Ar.objects.filter(select_brevet='brevet_ar_18')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_18':b_ar_18})

def b_ar_17(request):
    b_ar_17 = Brevet_Ar.objects.filter(select_brevet='brevet_ar_17')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_17':b_ar_17})

def b_ar_16(request):
    b_ar_16 = Brevet_Ar.objects.filter(select_brevet='brevet_ar_16')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_16':b_ar_16})

def b_ar_15(request):
    b_ar_15 = Brevet_Ar.objects.filter(select_brevet='brevet_ar_15')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_15':b_ar_15})


#page details slugs

def b_ar_d_20(request, slug):
    b_a_d_20 = Brevet_Ar.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_20':b_a_d_20})
def b_ar_d_19(request, slug):
    b_a_d_19 = Brevet_Ar.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_19':b_a_d_19})

def b_ar_d_18(request, slug):
    b_a_d_18 = Brevet_Ar.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_18':b_a_d_18})

def b_ar_d_17(request, slug):
    b_a_d_17 = Brevet_Ar.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_17':b_a_d_17})

def b_ar_d_16(request, slug):
    b_a_d_16 = Brevet_Ar.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_16':b_a_d_16})

def b_ar_d_15(request, slug):
    b_a_d_15 = Brevet_Ar.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_15':b_a_d_15})
