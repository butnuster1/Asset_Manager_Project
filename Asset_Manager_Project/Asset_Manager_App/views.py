from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

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
    
class RegisterPage(FormView):
    template_name = 'Asset_Manager_App/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    
    def form_valid(self, form): # this stuff redirects user once authenticated straight to index
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs): #this function prevents authenticated users from registering an account
        if self.request.user.is_authenticated:
            return redirect('index')
        return super(RegisterPage, self).get(*args, **kwargs)

class AssetList(ListView):
    model = Assets
    context_object_name = 'assets'
    
class AssetDetail(DetailView):
    model = Assets
    context_object_name = 'asset'
    
class AssetAdd(CreateView):
    model = Assets
    # fields = '__all__'
    fields = ['assetName', 'assetDescription', 'assetInStock']
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssetAdd, self).form_valid(form)
    

class AssetUpdate(UpdateView):
    model = Assets
    # fields = '__all__'
    fields = ['assetName', 'assetDescription', 'assetInStock']
    success_url = reverse_lazy('index')
    
class DeleteView(DeleteView):
    model = Assets
    context_object_name = 'asset'
    success_url = reverse_lazy('index')