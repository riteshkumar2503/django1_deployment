from django.shortcuts import render
from basic_app.forms import FormByUsingInbuiltUserModel, FormToAddStuffNotThereInTheInbuiltOne

# from django.core.urlresolvers import reverse
from django.urls import reverse

from django.contrib.auth.decorators import login_required
# login_required() does the following:
# 1. If the user isn't logged in, redirect to "settings.LOGIN_URL", passing the current absolute path in a query string parameter called "next".
# Example: /accounts/login/?next=/polls/3/
# 2.If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout


# Create your views here.

def index_view(request):
    return render(request, 'basic_app/index.html')


def register_view(request):
    is_registered= False
    form_inbuilt = FormByUsingInbuiltUserModel()  # agar ye line nahi daalenge to  GET request ke time,joki first time hoga, if condotion nahi execute hoga form_inbuilt create hi nahi hoga...other way is ki else laga lo jaisa yaha dikhaya hai: https://docs.djangoproject.com/en/3.2/topics/forms/
    form_toaddstuff = FormToAddStuffNotThereInTheInbuiltOne()

    #  The basic idea is that we check if there is a POST request and then perform some sort of action based off that information
    if request.method == 'POST':
        form_inbuilt = FormByUsingInbuiltUserModel(request.POST)
        form_toaddstuff = FormToAddStuffNotThereInTheInbuiltOne(request.POST)

        if form_inbuilt.is_valid() and form_toaddstuff.is_valid:
            result1 = form_inbuilt.save()
            print("qqqq>>>",result1, "wwww>>>",result1.password)
            result1.set_password(result1.password)
            result1.save()
            print("eeee>>>",result1, "rrrrr>>>",result1.password)

            result2 = form_toaddstuff.save(commit=False)  # we will set commit=False so we can manipulate the data before saving it to the database.
            result2.user_again = result1
            if 'profile_pic' in request.FILES:
                result2.profile_pic = request.FILES['profile_pic']
            result2.save()

            is_registered = True
        else:
            print ("error 1111", form_inbuilt.errors, "error 2222", form_toaddstuff.errors, )

    return render(request, 'basic_app/registration.html', {'userform_sent_by_view': form_inbuilt, 'userprofileinfoform_sent_by_view':form_toaddstuff,'is_registered_sent_by_view':is_registered })


def login_view(request):
    user123 = ''
    if request.method == 'POST':
        #  see basicforms project waha pe form tha to usko PEHLE, import karte the, FIR ye karte the>> form1 = FormNameEmailText(request.POST), FIR uske baad uska data nikalte the using this name = request.POST.get('name').....par yaha pe data direct aa raha hai by hitting an endpoint using actions..so direct 3rd step use kar lo
        username123 = request.POST.get('usernameee')
        password123 = request.POST.get('passworddd')
        user123 = authenticate(username=username123, password=password123)
        if user123:
            print ("here 11")
            if user123.is_active:
                print("here 22", user123)
                print ("here 33", user123.is_authenticated)  # (template ke andar user123.is_authenticated nahi hoga unlike yaha....html template ke andar "user" inbuilt name hai by default...user is automatically passed back to the backend using Django and its decorators-->
                login(request, user123)
                # return HttpResponseRedirect("https://www.cricbuzz.com/") # hardcode nahi karne ke liye reverse lagao
                # return HttpResponseRedirect(reverse('basic_app123:register_view_pattern_name'))
                return HttpResponseRedirect(reverse("index_view_pattern_name"))  # ye index view ka url pattern project folder me hai..not in app folder, isliye appname:viewname nahi kar rahe..nahi to karna padta
                # isko old style se bhi redirect karne ka try karo ek baar
            else:
                print("22222")
                return HttpResponse("account not active")

        else:
            print ("someone tried to with username: {} and password: {} and failed".format(username123, password123))
            return HttpResponse("invalid login details supplied")

    else:
        return render(request, 'basic_app/login.html')


@login_required
# so that there is no option to logout when no one is logged in..infact this decorators can be used on any view to give access to those pages only if they are logged in..have showen in the below view
# LOGIN_URL in settings.py define the  URL  where requests are redirected for login when using the login_required() decorator.
# eg. http://127.0.0.1:8000/special try this one whhose view is just after this view..ye login page pe bhej dega agar logged in nahi hai to..fir login karo...fir isko hit karo to sahi jagah bhejega
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_view_pattern_name'))
    # return HttpResponse("bang")

@login_required
def special_view_with_login_required(request):
    print("speciallll")
    return HttpResponse("NICE!! YOU ARE LOGGED IN")




