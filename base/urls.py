from django.urls import include, path
from . import views


urlpatterns=[
  path('', views.login_view , name='login'),
  path('signup/', views.signup, name='signup'),

]