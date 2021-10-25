from django.db import models
from django.contrib.auth.models import User   # this imports the inbuilt User class from the already  built-in Authentication and Authorization model set in place which we see when we open the admin page


#  Sometimes we want to add more attributes to a user,we can do this in our applications models.py file by creating another class that has a relationship to the 'User' class

class ModelToAddStuffToInBuiltUserModel(models.Model):
    user_again = models.OneToOneField(User, on_delete=models.CASCADE)  # creating a one to one relation with the inbuilt model
    # additions
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(blank=True, upload_to='profile_pics' )
    # def __str__(self):
    #     return self

