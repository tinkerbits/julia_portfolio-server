from django.urls import path
from .views import HomeView, ArtworkListView, ArtworkDetailView

urlpatterns = [
    path('portfolio/', ArtworkListView.as_view(), name='artwork_list'),
    path('artwork/<int:pk>/<str:slug>/', ArtworkDetailView.as_view(), name='artwork_detail'),
    path('', HomeView.as_view(), name='home'),
]