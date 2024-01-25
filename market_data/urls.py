from django.urls import path
from .views import dashboard,table_details,table_details2,get_data_for_popup

urlpatterns = [
    #path('table2/', oneweek, name='oneweek'),
    path('table/', dashboard, name='dashboard'),
    path('table/<str:table_name>/', table_details, name='table_details'),
    path('', table_details2, name='table_details2'),
    path('get_data_for_popup/<str:table_name>/', get_data_for_popup, name='get_data_for_popup'),
    #path('popup_content_view/<str:table_name>/', popup_content_view, name='popup_content_view'),
    ]