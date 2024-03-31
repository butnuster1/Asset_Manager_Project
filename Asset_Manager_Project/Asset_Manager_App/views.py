from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Assets


def index(request):
    asset = Assets.objects.all()

    return render(
        request,
        "Asset_Manager_App/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        
        {
            'title' : "Dickson College Asset Manager! ",
            'message' : "Welcome to the Dickson College Asset Manager",
            'content' : "table",
            'assetList': asset
        }
    )

def schedule(request):
    return render(
        request,
        "Asset_Manager_App/schedule.html",
        {
            'title' : "Schedule page",
            'content' : "Add events to your schedule."
        }
    )

class AssetAdd(CreateView):
    model = Assets
    fields = '__all__'
    success_url = reverse_lazy('schedule')
    
    