from django.urls import  path
from . import views 
urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.custom_login, name='login'),
    path('signup/', views.signup, name = "signup"),
    path('logout/',views.LogoutPage,name="logout"),
    path('project/add',views.project_add, name = "project_add"),
    path('test/', views.test, name='test'),

]