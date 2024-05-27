from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('cursy/', views.cursy_page, name='cursy_page'),
    path('aboutus/', views.aboutus_page, name='aboutus_page'),
    path('cursy/details/<int:pk>/', views.curs_details, name='curs_details'),
]
