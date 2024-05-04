from django.shortcuts import render, redirect
from .models import Order
from django.http import HttpResponse, JsonResponse
from .forms import OrderForm
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework import generics
from .serializers import OrderListApi


def Index(request):
    query = request.GET.get('q')
    if query:
        list = Order.objects.all().order_by('-id').filter(
            Q(name__icontains=query)| 
            Q(last__icontains=query) | 
            Q(phone__icontains=query) | 
            Q(datetime__icontains=query)
        )
    else :
        list = Order.objects.all().order_by('-id')
    paginator = Paginator(list, 10) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    num_pages = paginator.num_pages
    contex = {
       'list':page_obj,
       'num_pags':num_pages,
       'page_number':page_number,
       'q':query
    }
    
    return render(request, 'index.html', contex)


def AddViews(request):
    if request.method == 'POST':
        name = request.POST[ 'name' ]
        last = request.POST[ 'last' ]
        phone = request.POST[ 'phone' ]
        addres = request.POST[ 'addres' ]
        liter = request.POST[ 'liter' ]

        save_order = Order(
            name = name,
            last=last,
            phone=phone,
            addres=addres,
            liter=liter
        )
        save_order.save()

        succses = 'Save ' + name
        print(succses)
        return HttpResponse(succses)
    else :
        succses = 'Please try again later'
        return HttpResponse(succses)


        
def EditViews(request):
    if request.method == 'POST':
        name = request.POST[ 'name_id' ]
        last = request.POST[ 'last_id' ]
        phone = request.POST[ 'phone_id' ]
        addres = request.POST[ 'addres_id' ]
        liter = request.POST[ 'liter_id' ]
        id_edit = request.POST[ 'id_edit' ]

        save_order = Order(
            id = id_edit,
            name = name,
            last=last,
            phone=phone,
            addres=addres,
            liter=liter
        )
        save_order.save()

        succses = 'Edit order ' + name
        print(succses)
        return HttpResponse(succses)
    else :
        succses = 'Please try again later'
        return HttpResponse(succses)
    
        


def DeleteViews(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            product = Order.objects.get(id=id)
            product.delete()
            delete = 'Delete ' + product.name
            return HttpResponse(delete)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def CheckView(request):
    if request.method == 'POST':
        checkbox_values = request.POST.getlist('task_ids[]')  # Checkboxlar nomi
        print(checkbox_values)
        status = '1'
        for task_id in checkbox_values:
            task = Order.objects.get(id=task_id)
            task.delete()
        return HttpResponse(status)    
    else :
        status = '0'
        return HttpResponse(status)    




def get_product(request, id):
    try:
        order = Order.objects.get(id=id) 
        return JsonResponse({
            'name': order.name,
            'last': order.last,
            'phone': order.phone,
            'addres': order.addres,
            'liter': order.liter,
            'id': order.id})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found'}, status=404)




def HomeViews(request):
    order = Order.objects.all()
    total_sum = sum(list_number.liter for list_number in order)
    total_records = len(order)
    # print(total_records)
    contex = {
        'total_order':total_records,
        'total_sum':total_sum,
    }
    return render(request, 'home.html', contex)

# Api

class ApiListViews(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-id')[:1]
    serializer_class = OrderListApi