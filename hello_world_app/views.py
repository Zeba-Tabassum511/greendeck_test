from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .form import StudentRegistration
from .models import data
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import FormView


@csrf_exempt
def add(request):
    if request.method =='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request,'test_App/add_show.html',{'form':fm})





@csrf_exempt
def add_show(request):
    if request.method == 'POST':
        post = data()
       
        post.name = request.POST.get('name')
        print( post.name)
        post.brand_name = request.POST.get('brand_name')
        post.regular_price_value = request.POST.get('regular_price_value')
        post.offer_price_value = request.POST.get('offer_price_value')
        post.currency = request.POST.get('currency')
        post.classification_l1 = request.POST.get('classification_l1')
        post.classification_l2 = request.POST.get('classification_l2')
        post.classification_l3 = request.POST.get('classification_l3')
        post.classification_l4 = request.POST.get('classification_l4')
        post.image_url = request.POST.get('image_url')
        post.save()
        post = StudentRegistration()
    else:
        post = StudentRegistration()
    stud = data.objects.all()
    return render(request,'test_App/all_data.html',{'form':[post], 'stu':stud})
#Delete Function:
def delete_data(request,id):
    if request.method=='POST':
        pi = data.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')
#Update Function
def update_edit(request,id):
    if request.method=='POST':
        pi =data.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi =data.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
    return render(request , 'test_App/update.html',{'form':fm})
