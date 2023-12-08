from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'), 
    path('properties/', views.properties, name='property'), 
    path('about/', views.about, name='about'), 
    path('designs/', views.designs, name='designs'), 
    path('commercial/', views.commercials, name='commercial'), 
    path('residential/', views.residentials, name='residential'), 
    path('interior', views.interior, name='interior'), 
    path('contact', views.contact, name='contact'), 
    path('properties/<slug:property_slug>', views.property_details, name='property_details'),
]