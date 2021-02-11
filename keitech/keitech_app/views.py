from django.shortcuts import render
from django.views.generic import TemplateView

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
