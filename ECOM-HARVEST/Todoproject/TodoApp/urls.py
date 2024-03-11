from django.urls import path
from . import views
app_name='shop'
urlpatterns = [
    path('',views.Home,name='home'),
    path('phone/',views.phone,name='phone'),
    path('<slug:c_slug>/',views.phone,name='product_by_category'),
    path('details/<int:id>',views.Details,name='details'),
   
   

]
