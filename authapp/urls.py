from django.urls import path
from authapp import views
from .views import portfolio

urlpatterns = [
  path('', views.Home, name="Home"),  # Root URL pattern 
  path('index.html', views.Home, name="Home"),
  path('contact.html',views.contact, name="contact"),
  path('portfolio.html',views.portfolio, name="portfolio"),
  path('portfolio.html',views.portfolio, name="portfolio"),
  path('services.html',views.services, name="services"),
]

