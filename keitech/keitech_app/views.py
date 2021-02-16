from django.shortcuts import render
from django.views.generic import TemplateView
from keitech_app.forms import SignUpForm

# Create your views here.


def index(request):
    """This will display the homepage on the browser"""
    return render(request, "keitech_app/index.html")

class Services(TemplateView):
    """This will display our services page on the browser"""
    template_name = 'keitech_app/services.html'

class About(TemplateView):
    """This will display the about us page on the browser"""
    template_name = 'keitech_app/about.html'

class Contacts(TemplateView):
    """This will display the contacts page on the browser"""
    template_name = 'keitech_app/contacts.html'

class QuestionAnsewer(TemplateView):
    """this will display the question and answer page on the browser"""
    template_name = 'keitech_app/questions.html'


def SignUp(request):
    """This will display the signup page and validate the form"""
    registered = False

    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)

        if signup_form.is_valid():
            """This will save the signup form in the database"""
            user = signup_form.save()
            user.set_password(user.password)
            user.save()


            registered = True
        else:
            print(signup_form.errors)
    else:
        signup_form = SignUpForm()

    return render(request, 'keitech_app/signup.html',{'signup_form':signup_form, 'registered':registered})
