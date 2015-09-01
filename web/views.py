from string import Template

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail

from web.models import WebsiteEmailForm

@require_http_methods(["GET"])
def home(request):
    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def mail(request):
    if request.method == "POST":
        f = WebsiteEmailForm(request.POST)
        f.save()

    return render(request, 'thanks.html')
