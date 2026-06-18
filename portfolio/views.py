from django.shortcuts import render, get_object_or_404
from .models import Project, Contact
from django.contrib import messages

# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'portfolio/project_detail.html', {'project': project})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        messages.success(request, "Connexion etablie. Votre message a et transmis a Linx !")
        
    return render(request, 'portfolio/contact.html')