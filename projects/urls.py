from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
]
# we used the <int:pk> notation. This just tells Django that the value passed 
# in the URL is an integer, and its variable name is pk.
