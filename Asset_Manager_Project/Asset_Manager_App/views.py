from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Assets

@login_required(login_url="/login/") #users are unable to view the page until they are logged in https://docs.djangoproject.com/en/dev/topics/auth/default/#auth-web-requests
def index(request):
    user = request.user
    assets = Assets.objects.filter(user=user)
    stock_count = Assets.objects.filter(assetInStock=False).count()  # Count assets where complex is False
    # temp = Assets.objects.all()
    
    context = {
        'title': "Dickson College Asset Manager!",
        'message': "Welcome to the Dickson College Asset Manager",
        'content': "table",
        'assetList': assets,  # Use filtered assets instead of all assets
        'assets': assets,
        'count': stock_count
    }
    
    return render(request, "Asset_Manager_App/index.html", context)
    """
    return render(
        request,
        "Asset_Manager_App/index.html",  # Relative path from the 'templates' folder to the template file
        # "index.html", # Use this code for VS 2017 15.7 and earlier
        
        {
            'title' : "Dickson College Asset Manager! ",
            'message' : "Welcome to the Dickson College Asset Manager",
            'content' : "table",
            'assetList': temp
        }
    )
"""

def schedule(request):
    return render(
        request,
        "Asset_Manager_App/schedule.html",
        {
            'title' : "Schedule page",
            'content' : "Add events to your schedule."
        }
    )


# class based view method for restricting data to specific users
#def get_context_data(self, **kwargs):
 #   context = super().get_context_data(**kwargs)
 #   context['assets'] = ['assets'].filter(user=self.request.user)
 #   context['count'] = ['assets'].filter(complete=False).count()
 #   return context

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