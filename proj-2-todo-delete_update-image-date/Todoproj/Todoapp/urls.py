from . import views
from django.urls import path

urlpatterns = [
    
    path('',views.Home,name='home'),
    path('update/<int:id>',views.Update,name='update'),
    path('delete/<int:id>',views.Delete,name='delete'),

   
]