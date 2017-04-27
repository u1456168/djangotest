from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from hotel.models import Category
from hotel.models import Catform

def index(request):
        category_list = Category.objects.all()
        context_dict = {'categories': category_list}
        return render(request, 'hotel/index.html', context_dict)
def hotelcreate(request):
    if request.method == "GET":
        form = Catform();
        return render(request, 'hotel/addcat.html', {'form':form});
    elif request.method == "POST":
        form = Catform(request.POST);
        form.save();
        return redirect('index')
def hoteldetails(request, pk):

    #thehotel = Category.objects.filter(id = pk)[0]
    thehotel = Category.objects.get(id = pk)
    context = {'category': thehotel}
    return render(request, 'hotel/hoteldetails.html', context)
