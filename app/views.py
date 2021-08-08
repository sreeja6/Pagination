from django.shortcuts import render,redirect
from app.forms import Productform
from app.models import ProductModel
from django.core.paginator import Paginator





def add_pro(request):
    res = ProductModel.objects.all()
    page_no = request.GET.get("pno")
    pg = Paginator(res, 2)
    pa_range = pg.page_range
    if page_no:
        page = pg.page(page_no)
    else:
        page = pg.page(1)
    return render(request,"add_pro.html",{"form": Productform(),"s":page,"pr": pa_range})
def save_prod(request):
    ef = Productform(request.POST,request.FILES)
    if ef.is_valid():
        ef.save()
        return redirect('main')
    else:
        return render(request,"add_pro.html",{"form": ef})