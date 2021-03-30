from django.shortcuts import render
from django.views.generic import TemplateView
from keitech_app.forms import SignUpForm, ContactForm, NewsLetterForm

# Create your views here.


def index(request):
    """This will display the homepage on the browser"""
    if request.method == 'POST':
        newsletterform = NewsLetterForm(data=request.POST)
        if newsletterform.is_valid():
            """this will save the valid newsletter in the database"""
            newsletter = newsletterform.save()
        else:
            print(newsletterform.errors)
    else:
        newsletterform = NewsLetterForm()
    return render(request, "keitech_app/index.html", {'newsletterform':newsletterform})



class Services(TemplateView):
    """This will display our services page on the browser"""
    template_name = 'keitech_app/services.html'

class About(TemplateView):
    """This will display the about us page on the browser"""
    template_name = 'keitech_app/about.html'


class QuestionAnsewer(TemplateView):
    """this will display the question and answer page on the browser"""
    template_name = 'keitech_app/questions.html'


def Contacts(request):
    """This will display the contact us page on the browser"""
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            """this will save the valid contact us form in the database"""
            contact = contact_form.save()
        else:
            print(contact_form.errors)
    else:
        contact_form = ContactForm()

    return render(request, 'keitech_app/contacts.html',{'contact_form':contact_form})



def SignUp(request):
    """This will display the signup page and validate the form"""
    registered = False

    if request.method == 'POST':
        signup_form = SignUpForm(data=request.POST)

        if signup_form.is_valid():
            """This will save the valid signup form in the database"""
            user = signup_form.save()


            registered = True
        else:
            print(signup_form.errors)
    else:
        signup_form = SignUpForm()

    return render(request, 'keitech_app/signup.html',{'signup_form':signup_form, 'registered':registered})
