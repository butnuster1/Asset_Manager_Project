from django.db import models
from django.contrib.auth.models import User # We are using the default Django user authentication model
# Create your models here.

class Assets(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # deleting all assets under user's name if user is deleted. Cascade deletes assets and SET_NULL keeps assets.
    assetName = models.CharField(max_length=200)
    assetDescription = models.TextField(null=True, blank=True)
    assetInStock = models.BooleanField(default=False)
    assetAdded = models.DateTimeField(auto_now_add=True) #auto_now_add allows the system to automatically add the date it was added
    

    def __str__(self):
        return self.assetName
    
    class Meta:
        ordering = ['assetInStock'] #orders the assets by whether they are in stock or not
        

# REMEBER: running any change to this page you have to rerun makemigrations and migrate to commit changes