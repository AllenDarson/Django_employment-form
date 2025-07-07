from django.contrib import admin
from django.urls import path
from app_sqlform.views  import form ,table_data,show_data,add_details,show_details,find_person,update_all,update_employee,confirm_delete,delete_data

urlpatterns = [
    path('form',form),
    path('table_data',table_data),
    path('show_data',show_data),
    path('add_details',add_details),
    path('show_details',show_details),
    path('find_person',find_person),
    path('update_all/<int:id>',update_all),
    path('update_employee',update_employee),
    path('confirm_delete/<int:id>',confirm_delete),
    path('delete_data/<int:id>',delete_data)
]