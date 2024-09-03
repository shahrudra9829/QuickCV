from django.urls import path
from . import views
urlpatterns = [
    path('',views.go,name="go"),
    path('form/',views.accept,name="accept"),
    path('form/resume/<int:profile_id>/',views.resume,name="resume"),
    path('form/resume/<int:profile_id>/download_pdf/', views.download_pdf, name='download_pdf'),
]