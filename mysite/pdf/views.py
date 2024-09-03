from django.shortcuts import render,redirect,get_object_or_404
from .models import Profile
from django.template import loader
import pdfkit
from django.http import HttpResponse

# Create your views here.

def go(request):
    return render(request,'pdf/home.html')

def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        email=request.POST.get("email","")
        phone=request.POST.get("phone","")
        summary=request.POST.get("summary","")
        degree=request.POST.get("degree","")
        school=request.POST.get("school","")
        university=request.POST.get("university","")
        previous_work=request.POST.get("previous_work","")
        skills=request.POST.get("skills","")

        profile = Profile(name=name,email=email,phone=phone,summary=summary,degree=degree,school=school,university=university,previous_work=previous_work,skills=skills)
        profile.save()
        return redirect('resume', profile_id=profile.id)
    return render(request,'pdf/accept.html')

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