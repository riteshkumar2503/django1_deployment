from django import forms
from django.contrib.auth.models import User  # ye wala to inbuilt model hai
from basic_app.models import ModelToAddStuffToInBuiltUserModel


# pehla form to INBUILT wale model se bana liya
class FormByUsingInbuiltUserModel(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User  # ye wala to inbuilt model hai
        fields = ('username', 'email', 'password')
        # fields = "__all__"  # agar saare fields chahiye to


# doosra wala form jisme extra parameters hai wo CREATED model se bana liya..par take note ki while creating the doosra model, usko link kar diya hai inbuilt wale model se, by using user_again = models.OneToOneField(User)
class FormToAddStuffNotThereInTheInbuiltOne(forms.ModelForm):
    class Meta():
        model = ModelToAddStuffToInBuiltUserModel
        fields = ('portfolio_site', 'profile_pic')
        # fields = "__all__"

