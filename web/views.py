from string import Template

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.mail import send_mail

@require_http_methods(["GET"])
def home(request):
    return render(request, 'index.html')


@require_http_methods(["GET", "POST"])
def mail(request):
    RECIPIENTS = (
        'raymond@blueshiftedtech.com',
        'david@blueshiftedtech.com',
        'brian@blueshiftedtech.com'
    )

    message_template = Template("""
    Hello,

        It's bluebot again. We have a new request coming in 
        from the Blushift website. 
        
        This time it's from $name.
        Their email is $email.

        This is what they had to say:
        
        >>>><<<<
        $message
        >>>><<<<

    Thanks,
    Bluebot
    """)

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        msg = message_template.substitute(
            name=name,
            email=email,
            message=message
        )

        send_mail("Bluebot: Web Request", msg, 
                "info@blueshiftedtech.com", RECIPIENTS)

    return render(request, 'thanks.html')
