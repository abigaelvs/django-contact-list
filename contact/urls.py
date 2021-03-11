from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('contact/detail/<slug>', views.contact_detail, name='contact-detail'),
    path('contact/add/', views.add_contact, name='add-contact'),
    path('contact/edit/<slug>', views.edit_contact, name='edit-contact'),
    path('contact/delete/<slug>', views.delete_contact, name='delete-contact')
]