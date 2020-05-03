from django.urls import path
from .views import HomeView, ArtworkListView, ArtworkDetailView, AboutView

urlpatterns = [
    path('portfolio/', ArtworkListView.as_view(), name='artwork_list'),
    path('artwork/<int:pk>/<str:slug>/', ArtworkDetailView.as_view(), name='artwork_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('', HomeView.as_view(), name='home'),
]