from django.urls import path
from . import views
urlpatterns = [
    path('',views.lista,name='lista'),
    path('dados/',views.dados, name='dados')
 
]
