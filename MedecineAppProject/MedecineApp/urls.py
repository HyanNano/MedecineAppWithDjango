from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from . import views

#app_name = "MedecineApp"
urlpatterns = [
    
    path("", views.index, name="index"),
    
    path('Rechercher/',views.rechercher, name='rechercher'),

    path('Search/',views.search, name='search'),
    
    path('Publish/', views.publish, name='publish'),
    
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    
    path('actualite/',views.actualite, name='actualite'),
    
    path('itineraires/', views.affichage_routes, name="itineraire"),
    
    path('testdist/',views.test_distance, name='testdistance'),
] 
