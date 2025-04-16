from django.urls import path
from .views import *
urlpatterns = [
    path('',go,name="go"),
    path('form/',accept,name="accept"),
    path('form/resume/<int:profile_id>/',resume,name="resume"),
    path('form/resume/<int:profile_id>/download_pdf/',download_pdf, name='download_pdf'),
]