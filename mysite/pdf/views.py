from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from django.template import loader
import pdfkit
from django.http import HttpResponse
from .form import *

# Create your views here.

def go(request):
    return render(request,'pdf/home.html')

def temp_list(request):
    return render(request,"pdf/dif_formate.html")

def accept(request):
    form = Details()
    if request.method=="POST":
        form = Details(request.POST)
        if form.is_valid():
            form_obj=form.save() 
        return redirect('resume', profile_id=form_obj.id)
    return render(request,'pdf/accept.html',{"form":form})

def resume(request,profile_id):
    user_profile=get_object_or_404(Profile,id=profile_id)
    return render(request,'pdf/resume.html',{'user_profile':user_profile})


def download_pdf(request,profile_id):
    user_profile = get_object_or_404(Profile, id=profile_id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': user_profile,'is_pdf': True})

    # Convert the HTML to a PDF
    pdf = pdfkit.from_string(html, False)

    # Create a response to download the PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{user_profile.name}_resume.pdf"'

    return response