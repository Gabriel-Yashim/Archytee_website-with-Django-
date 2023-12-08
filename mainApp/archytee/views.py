from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from .form import ContactForm
from django.core.mail import send_mail
from .models import RecentProjects, ClientFeedback, interiorProjects, designProjects, residentialProjects, commercialProjects, Properties, ClientForm


# Create your views here.
def index(request):
    recentProjects= RecentProjects.objects.all()
    clientFeedback = ClientFeedback.objects.all()
    
    return render(request, 'archytee/index.html', {'recentProjects': recentProjects, 'clientFeedback': clientFeedback})
    # return HttpResponse('Hello world')
    
def properties(request):
    return render(request, 'archytee/properties.html')

def about(request):
    return render(request, 'archytee/about.html')

def designs(request):
    design = designProjects.objects.all()
    
    return render(request, 'archytee/3D-designs.html', {'designs': design})

def commercials(request):
    commercials = commercialProjects.objects.all()
    
    return render(request, 'archytee/commercials.html', {'commercials': commercials})

def residentials(request):
    residentials = residentialProjects.objects.all()
    
    return render(request, 'archytee/residentials.html', {'residentials': residentials})

def interior(request):
    interiors = interiorProjects.objects.all()
    
    return render(request, 'archytee/interiors.html', {'interiors': interiors})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email notification to the admin
            subject = 'New Contact Form Submission'
            message = f'A new message has been submitted:\n\n{form.cleaned_data["message"]}'
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [settings.ADMIN_EMAIL]  # Replace with the admin's email address

            send_mail(subject, message, from_email, recipient_list)
            
            
            # You can include logic here for sending email notifications, etc.
            return render(request, 'archytee/contact.html', {'message_sent': True})
    else:
        form = ContactForm()
    return render(request, 'archytee/contact.html', {'form': form})

def properties(request):
    properties = Properties.objects.all()
    properties_sale = Properties.objects.filter(category='Sale')  # Filter properties for Sale category
    properties_lease = Properties.objects.filter(category='Lease')  # Filter properties for Lease category
    return render(request, 'archytee/properties.html', {'properties':properties, 'properties_sale': properties_sale, 'properties_lease': properties_lease})

def property_details(request, property_slug):
    print(property_slug)
    slug = Properties.objects.get(slug=property_slug)
    properties = Properties.objects.all()
    return render(request, 'archytee/property_details.html', {'slug': slug, 'properties':properties, 'property_slug':property_slug})

# def project_details(request, project_slug):
#     print(project_slug)
#     return render(request, 'archytee/project_details.html')