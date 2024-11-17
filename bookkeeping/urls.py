from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('properties/', views.properties, name='properties'),
    path('tenants/', views.tenants, name='tenants'),
    path('expenses/', views.expenses, name='expenses'),
    path('upload_statement/', views.upload_bank_statement, name='upload_statement'),
    path('add_property/', views.add_property, name='add_property'),
    path('add_tenant/', views.add_tenant, name='add_tenant'),
    path('add_expense_profile/', views.add_expense_profile, name='add_expense_profile'),
]
