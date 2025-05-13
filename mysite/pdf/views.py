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

# def accept(request):
#     form = Details()
#     if request.method=="POST":
#         form = Details(request.POST)
#         if form.is_valid():
#             # form_obj=form.save()
#             request.session['form_data']=form.cleaned_data 
#             return redirect('resume')
#     return render(request,'pdf/accept.html',{"form":form})

def accept(request):
    if request.method == "POST":
        form = Details(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            skills = request.POST.getlist("skills[]")
            # Use getlist to fetch all parallel entries
            degrees = request.POST.getlist("degree[]")
            field = request.POST.getlist("field[]")
            universities = request.POST.getlist("university[]")
            timeperiod = request.POST.getlist("timeperiod[]")

            education_list = []
            for degree,field, timeperiod, university in zip(degrees,field,universities,timeperiod):
                education_list.append({
                    "degree": degree,
                    "university": university,
                    "field":field,
                    "timeperiod":timeperiod
                })

            company = request.POST.getlist("company[]")
            designation = request.POST.getlist("designation[]")
            location = request.POST.getlist("location[]")
            duration = request.POST.getlist("duration[]")
            responsibility = request.POST.getlist("role[]")

            experience_list = []
            for company,designation,location,duration in zip(company,designation,location,duration):
                experience_list.append({
                    "company": company,
                    "designation": designation,
                    "location": location,
                    "duration": duration,
                    "responsibility": responsibility
                })

            
            data["experience"] = experience_list
            data["skills"] = skills
            data["education"] = education_list
            request.session['form_data'] = data
            return redirect('resume')
    else:
        form = Details()

    return render(request, 'pdf/accept.html', {"form": form})


def resume(request):
    form_data = request.session.get('form_data')
    if not form_data:
        return redirect('accept')
    return render(request,'pdf/resume.html',{'user_profile':form_data})


def download_pdf(request):
    form_data = request.session.get('form_data')
    if not form_data:
        return redirect('accept')
    
    # user_profile = get_object_or_404(Profile, id=profile_id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user_profile': form_data,'is_pdf': True})

    # Convert the HTML to a PDF
    pdf = pdfkit.from_string(html, False)

    # Create a response to download the PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{form_data["name"]}_resume.pdf"'

    return response