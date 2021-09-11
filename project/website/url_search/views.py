from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from django.db.models import Q 
from url_search.models import Url_list
import json
from django.shortcuts import redirect
# Create your views here.
def home(request):

    #results=Url_list.objects.all
    return render(request, "home.html")

def add(request):    
    val1 = request.POST['url_for']
    redirectStatus = request.POST.get('redirect', None)

    if redirectStatus == 'true':
        return redirect("https://"+val1+"/")
        
    results = Url_list.objects.filter(Q(name__startswith=val1))

    if results:
        return render(request,'results.html',{'results':results})

    else:
       return render(request,'results.html',{'data':val1})

def website_search(request):
    data = None
    # check if search request is ajax
    if request.is_ajax():
        # if request is a ajax get data by input value in search box
        q = request.GET.get('term', '')
        websites = Url_list.objects.filter(name__startswith=q)

        results = []
        # change collection to array 
        for site in websites:
            site_json = {}
            site_json = site.name
            results.append(site_json)
            data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    # return respone to ajax call in html frontend
    return HttpResponse(data, mimetype)