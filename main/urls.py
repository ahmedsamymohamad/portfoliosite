from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<slug:slug>', views.PortfolioDetailView.as_view(), name="portfolio-detail"),
    path('about/', views.AboutView.as_view(), name='about'),
    path('blog/<slug:slug>', views.BlogDetailView.as_view(), name='blog'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    
]
