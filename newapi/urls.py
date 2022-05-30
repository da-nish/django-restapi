from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from newapi import views


urlpatterns = [
    path('go/', views.userlist.as_view()),
    path('go/<pk>', views.userdata.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)