from django.shortcuts import render
from .models import Bepcar2015, Bepcar2016, Bepcar2017, Bepcar2018, Bepcar2019, Bepcar2020

def b_ar_20(request):
    b_ar_20 = Bepcar2020.objects.filter(status='published')[0:4]
    return render(request,'ar/cours_ar.html',{'b_ar_20' : b_ar_20,})
    
def b_ar_19(request):
    b_ar_19 = Bepcar2019.objects.filter(status='published')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_19':b_ar_19})

def b_ar_18(request):
    b_ar_18 = Bepcar2018.objects.filter(status='published')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_18':b_ar_18})

def b_ar_17(request):
    b_ar_17 = Bepcar2017.objects.filter(status='published')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_17':b_ar_17})

def b_ar_16(request):
    b_ar_16 = Bepcar2016.objects.filter(status='published')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_16':b_ar_16})

def b_ar_15(request):
    b_ar_15 = Bepcar2015.objects.filter(status='published')[0:4]
    return render(request, 'ar/cours_ar.html',{'b_ar_15':b_ar_15})


#page details slugs

def b_ar_d_20(request, slug):
    b_a_d_20 = Bepcar2020.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_20':b_a_d_20})
def b_ar_d_19(request, slug):
    b_a_d_19 = Bepcar2019.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_19':b_a_d_19})

def b_ar_d_18(request, slug):
    b_a_d_18 = Bepcar2018.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_18':b_a_d_18})

def b_ar_d_17(request, slug):
    b_a_d_17 = Bepcar2017.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_17':b_a_d_17})

def b_ar_d_16(request, slug):
    b_a_d_16 = Bepcar2016.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_16':b_a_d_16})

def b_ar_d_15(request, slug):
    b_a_d_15 = Bepcar2015.objects.get(slug=slug)
    return render(request, 'ar/cours_ar_d.html',{'b_a_d_15':b_a_d_15})
