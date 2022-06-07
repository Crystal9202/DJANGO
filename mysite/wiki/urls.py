from django.urls import path
from . import views

app_name = 'wiki'
urlpatterns = [
    #post views
    path('',views.wiki , name="wiki")
]