from django.urls import path
from . import views

# define a list of ulr patterns

urlpatterns = [
    path('', views.index,)
]