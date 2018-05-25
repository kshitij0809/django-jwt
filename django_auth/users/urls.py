from django.conf.urls import url
from .views import CreateUserAPIView
from . import views
 
urlpatterns = [
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^token_generation/$', views.authenticate_user),

]