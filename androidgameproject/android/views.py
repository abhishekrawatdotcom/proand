from django.shortcuts import render
from android.models import Users,Games,File

# Create your views here.
def gamepro(request):
    Files=File.objects.all()
    return render(request,'index.html',{'Files':Files})


def searchmatch(query, item):
    if Users.objects.filter(Games__icontains=query) | Users.objects.filter(Username__icontains=query):
        return True
    else:
        return False


def search(request):
    query=request.GET.get('search')
    prot = Users.objects.filter(Games__icontains=query) | Users.objects.filter(Username__icontains=query)
    prod=[item for item in prot if searchmatch(query,item)]

    return render(request,'search.html',{'prod':prod})

def imageview(request, myid):
    prod=File.objects.filter(id= myid)
    return render(request,'image.html',{'prodd':prod})
