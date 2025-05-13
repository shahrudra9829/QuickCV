from django.urls import path
from .views import *
urlpatterns = [
    path('',go,name="go"),
    path('form/template/',temp_list,name='template_list'),
    path('form/',accept,name="accept"),
    path('form/resume/',resume,name="resume"),
    path('form/resume/download_pdf/',download_pdf, name='download_pdf'),
]