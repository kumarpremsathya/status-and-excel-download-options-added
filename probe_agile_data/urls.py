from django.urls import path
# from .views import show
from probe_agile_data import views

urlpatterns = [
    
    path('rbinewhome/', views.rbinewhome, name='rbinewhome'),
    path('rbi_tab/', views.rbi_tab, name='rbi_tab'),
    path('rbiget_data_for_popup1/<str:source_name>/', views.rbiget_data_for_popup1, name='rbiget_data_for_popup1'),
    path('rbinewfema_datefilter/', views.rbinewfema_datefilter, name='rbinewfema_datefilter'),
    path('rbinewecb_datefilter/', views.rbinewecb_datefilter, name='rbinewecb_datefilter'),
    path('rbinewodi_datefilter/', views.rbinewodi_datefilter, name='rbinewodi_datefilter'),
    path('rbinewstartupindia_datefilter/', views.rbinewstartupindia_datefilter, name='rbinewstartupindia_datefilter'),


]



