from django.urls import path
from .views import ArtworkListView, HomeView

urlpatterns = [
    path('portfolio/', ArtworkListView.as_view(), name='artwork_list'),
    path('', HomeView.as_view(), name='home'),
]