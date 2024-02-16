from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Contact
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail


def homepage(request):
    return render(request, 'home/index.html')


def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_login")
    else:
        form = CreateUserForm()

    context = {'registerform': form}
    return render(request, 'home/register.html', context=context)


def user_login(request):  # Renamed from 'login' to 'user_login'
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if user.is_staff:
                    return redirect("admin:index")  # Redirect to admin dashboard
                else:
                    return render(request, 'home/dashboard.html')

    else:
        form = LoginForm()

    context = {'loginform': form}
    return render(request, 'home/login.html', context=context)


@login_required(login_url='/user_login')  # Adjusted login URL to 'user_login'
def user_logout(request):
    logout(request)
    return redirect("")


@login_required(login_url='/user_login')  # Adjusted login URL to 'user_login'
def dashboard(request):
    return render(request, 'home/dashboard.html')


@login_required(login_url='/user_login')
def geolocate(request):
    return render(request, 'home/geolocate.html')


@login_required(login_url='/user_login')
def locateme(request):
    return render(request, 'home/locateme.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')


def submit_contact(request):
    if request.method == 'POST':
        name = request.POST['w3lName']
        email = request.POST['w3lSender']
        subject = request.POST['w3lSubject']
        message = request.POST['w3lMessage']
        admin_reply = models.TextField(blank=True)

        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        # return HttpResponse("Form submitted successfully")

    return render(request, 'home/contact.html')


def admin_view(request, form_id):
    form_instance = get_object_or_404(Contact, id=form_id)

    if request.method == 'POST':
        admin_reply = request.POST.get('admin_reply', '')
        form_instance.admin_reply = admin_reply
        form_instance.save()

        # Send email to the user using the admin reply as the email subject and body
        send_mail(
            f'Re: {admin_reply}',  # Use the admin reply from the form as the email subject
            admin_reply,  # Use the admin reply from the form as the email body
            'your_admin_email@example.com',  # Sender's email
            [form_instance.email],  # Recipient's email
            fail_silently=False,
        )

        messages.success(request, 'Reply sent successfully')  # Add success message

        return HttpResponseRedirect(reverse('admin:home_contact_changelist'))  # Redirect to admin contact page

    return render(request, 'home/admin_view_template.html', {'form_instance': form_instance})
