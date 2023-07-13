from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hello from prettyPrinted',
              'hello there. this us an automated message',
              'tilina.com',
              ['gokas38987@kameili.com'],
              fail_silently=False)
    return render(request, 'send/index.html')
