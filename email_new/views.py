from django.shortcuts import render
from django.core.mail import send_mail


def enter_email(request):
    return render(request, 'email_new/home.html')


def receive_email_data(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        destination = request.POST.get('destination')
        subject = request.POST.get('subject')
        email_text = request.POST.get('email_text')
        send_mail(subject, email_text, email, [destination], fail_silently=False)
        return render(request, 'email_new/submit.html')
