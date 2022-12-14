from django.urls import path
from .views import HomeView, ArtworkListView, ArtworkDetailView, AboutView, ContactView, ContactSuccessView, RobotView

urlpatterns = [
    path('portfolio/', ArtworkListView.as_view(), name='artwork_list'),
    path('artwork/<int:pk>/<slug:slug>/', ArtworkDetailView.as_view(), name='artwork_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('success/', ContactSuccessView.as_view(), name='contact_success'),
    path('robots.txt', RobotView.as_view(), name='robots.txt'),
    path('', HomeView.as_view(), name='home'),
]