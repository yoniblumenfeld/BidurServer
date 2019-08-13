from django.urls import path
from . import views

urlpatterns = [
    path('search/',views.ScrapersData.as_view(),name='search')
]