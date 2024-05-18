from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

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

class CustomLoginView(LoginView):
    template_name = 'Asset_Manager_App/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('index')

class AssetList(ListView):
    model = Assets
    context_object_name = 'assets'
    
class AssetDetail(DetailView):
    model = Assets
    context_object_name = 'asset'

class AssetAdd(CreateView):
    model = Assets
    fields = '__all__'
    success_url = reverse_lazy('index')
    
class AssetUpdate(UpdateView):
    model = Assets
    fields = '__all__'
    success_url = reverse_lazy('index')
    
class DeleteView(DeleteView):
    model = Assets
    context_object_name = 'asset'
    success_url = reverse_lazy('index')