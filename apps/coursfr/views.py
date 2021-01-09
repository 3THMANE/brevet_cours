from django.shortcuts import render
from .models import Bepcfr2015, Bepcfr2016, Bepcfr2017, Bepcfr2018, Bepcfr2019, Bepcfr2020

def b_fr_20(request):
    b_fr_20 = Bepcfr2020.objects.filter(status='published')[0:4]
    return render(request,'fr/cours_fr.html',{'b_fr_20' : b_fr_20,})
    
def b_fr_19(request):
    b_fr_19 = Bepcfr2019.objects.filter(status='published')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_19':b_fr_19})

def b_fr_18(request):
    b_fr_18 = Bepcfr2018.objects.filter(status='published')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_18':b_fr_18})

def b_fr_17(request):
    b_fr_17 = Bepcfr2017.objects.filter(status='published')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_17':b_fr_17})

def b_fr_16(request):
    b_fr_16 = Bepcfr2016.objects.filter(status='published')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_16':b_fr_16})

def b_fr_15(request):
    b_fr_15 = Bepcfr2015.objects.filter(status='published')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_15':b_fr_15})


#page details slugs

def b_fr_d_20(request, slug):
    b_f_d_20 = Bepcfr2020.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_20':b_f_d_20})
def b_fr_d_19(request, slug):
    b_f_d_19 = Bepcfr2019.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_19':b_f_d_19})

def b_fr_d_18(request, slug):
    b_f_d_18 = Bepcfr2018.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_18':b_f_d_18})

def b_fr_d_17(request, slug):
    b_f_d_17 = Bepcfr2017.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_17':b_f_d_17})

def b_fr_d_16(request, slug):
    b_f_d_16 = Bepcfr2016.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_16':b_f_d_16})

def b_fr_d_15(request, slug):
    b_f_d_15 = Bepcfr2015.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_15':b_f_d_15})
