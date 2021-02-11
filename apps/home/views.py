from django.shortcuts import render
from .models import Contact

# from apps.coursar.models import Bepcar2020
from apps.coursfr.models import Cours_Fr
from apps.coursar.models import Cours_Ar
# from django.http import JsonResponse
# from django.core import serializers

# Create your views here.
def home(request):
    return render(request, 'home/index.html',{
                         
                        })



def courses(request):
    cours_ar = Cours_Ar.objects.all()
    cours_fr = Cours_Fr.objects.all()
    return render(request, 'home/all_c.html',{
        'cours_ar':cours_ar,
        'cours_fr':cours_fr
        })

# def c_a_detail(request, slug):
#     c_a_detail = Cours_Ar.objects.get(slug=slug)
#     return render(request, 'home/all_d.html',{
#         'c_a_detail':c_a_detail
        
#         })
# def c_f_detail(request, slug):
#     c_f_detail = Cours_Fr.objects.get(slug=slug)
#     return render(request, 'home/all_d.html',{
#         'c_f_detail':c_f_detail
        
#         })


# def nav(request): 
#     b_ar_20 = Bepcar2020.objects.all()[:1]
#     # cours_ar = Coursar.objects.all()[0:2]
#     # cours_fr = Coursfr.objects.all()[0:2]
#     # cours_fr = Coursfr.objects.all()
    
#     # .order_by(-create).[0:5]
#     return render(request, 'navbar.html',{
#                           'b_ar_20':b_ar_20,
#                         #   'cours_fr':cours_fr
#                         })
    
# def b_ar_d_20(request, slug):
#     b_a_d_20 = Bepcar2020.objects.get(slug=slug)
#     return render(request, 'ar/bepc_ar_detail_20.html',{'b_a_d_20':b_a_d_20})
                   
# def load(request): 
#     offset = int(request.POST['offset'])
#     offset = int(request.POST['offset'])
#     limit =2
#     cours_ar = Coursar.objects.all()[offset:limit+offset]
#     total = Coursar.objects.count()
#     cours_fr = Coursfr.objects.all()[offset:limit+offset]
#     total2 = Coursfr.objects.count()
#     data={}
#     cours = serializers.serialize('json',cours_ar)
#     cours2 = serializers.serialize('json',cours_fr)

#     return JsonResponse(data={
#         'cours_ar':cours,
#         'totalr':total,
#         'cours_fr':cours2,
#         'totalr2':total2
#     })



def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        message = request.POST.get("message")
        instance = Contact(name=name, phone=phone, email=email, message=message)
        instance.save()
    return render(request, 'home/contact.html')
