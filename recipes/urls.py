from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.home),
    path('recipes/<int:id>/', v.recipe),
]
