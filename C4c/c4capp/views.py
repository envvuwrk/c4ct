from django.http import HttpResponse, Http404
from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def products(request):
    return render(request, "products.html")


def support(request):
    return render(request, "support.html")


def clients(request):
    return render(request, "clients.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        try:
            phone = request.POST['phone']
            message = request.POST['message']
        except MultiValueDictKeyError:
            phone = False
            message = False
        template = get_template('contactus2.txt')
        context = {'name': name, 'email': email, 'phone': phone, 'message': message}
        content = template.render(context)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.send()
        messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
    return render(request, 'contact.html')
