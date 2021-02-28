from django.shortcuts import render
from .models import Brevet_Fr
from .models import Cours_Fr

def coursesfr(request):
    cours_fr = Cours_Fr.objects.all()
   
    return render(request, 'fr/all_fr.html',{
        'cours_fr':cours_fr,
        
        })

def c_f_detail(request, slug):
    c_f_detail = Cours_Fr.objects.get(slug=slug)
    return render(request, 'home/all_d.html',{
        'c_f_detail':c_f_detail
        
        })

def b_fr_20(request):
    b_fr_20 = Brevet_Fr.objects.filter(select_brevet='brevet_fr_20')[0:4]
    return render(request,'fr/cours_fr.html',{'b_fr_20' : b_fr_20,})
    
def b_fr_19(request):
    b_fr_19 = Brevet_Fr.objects.filter(select_brevet='brevet_fr_19')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_19':b_fr_19})

def b_fr_18(request):
    b_fr_18 = Brevet_Fr.objects.filter(select_brevet='brevet_fr_18')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_18':b_fr_18})

def b_fr_17(request):
    b_fr_17 = Brevet_Fr.objects.filter(select_brevet='brevet_fr_17')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_17':b_fr_17})

def b_fr_16(request):
    b_fr_16 = Brevet_Fr.objects.filter(select_brevet='brevet_fr_16')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_16':b_fr_16})

def b_fr_15(request):
    b_fr_15 = Brevet_Fr.objects.filter(select_brevet='brevet_fr_15')[0:4]
    return render(request, 'fr/cours_fr.html',{'b_fr_15':b_fr_15})


#page details slugs

def b_fr_d_20(request, slug):
    b_f_d_20 = Brevet_Fr.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_20':b_f_d_20})
def b_fr_d_19(request, slug):
    b_f_d_19 = Brevet_Fr.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_19':b_f_d_19})

def b_fr_d_18(request, slug):
    b_f_d_18 = Brevet_Fr.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_18':b_f_d_18})

def b_fr_d_17(request, slug):
    b_f_d_17 = Brevet_Fr.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_17':b_f_d_17})

def b_fr_d_16(request, slug):
    b_f_d_16 = Brevet_Fr.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_16':b_f_d_16})

def b_fr_d_15(request, slug):
    b_f_d_15 = Brevet_Fr.objects.get(slug=slug)
    return render(request, 'fr/cours_fr_d.html',{'b_f_d_15':b_f_d_15})
