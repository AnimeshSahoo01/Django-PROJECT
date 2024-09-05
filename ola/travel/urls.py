from django.urls import path
from travel.views import *
app_name='ghumi'
urlpatterns=[
   path('buli/',buli,name='buli'),
]