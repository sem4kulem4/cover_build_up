from django.urls import path
from .views import CurveAPI

app_name = 'api'
urlpatterns = [
   path('v1/curves/', CurveAPI.as_view()),
]
