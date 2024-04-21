from django.urls import path 
from classification import views

app_name="classification"

urlpatterns = [
    path("predict/", views.predict, name="predict"),
]

