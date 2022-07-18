from django.urls import path
from NimapApp import views
from NimapApp.views import Home,Add_info,Delete_info,EditEmployee


urlpatterns = [
    path('',views.client_registration,name='registration'),
    path('login/',views.client_login,name='login'),
    path('logout/',views.client_logout,name='logout'),
    path('home/',Home.as_view(),name='home'),
    path('add/',Add_info.as_view(),name='add-info'),
    path('delete/',Delete_info.as_view(),name='delete-info'),
    path('edit/<int:id>/',EditEmployee.as_view(),name='edit-info')

    
    
]
