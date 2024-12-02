from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Properties
    path('properties/', views.properties, name='properties'),
    path('add_property/', views.add_property, name='add_property'),
    path('edit_property/', views.edit_property, name='edit_property'),
    path('delete_property/<int:pk>/', views.delete_property, name='delete_property'),

    # Units
    path('units/', views.units, name='units'),
    path('add_unit/', views.add_unit, name='add_unit'),
    path('edit_unit/', views.edit_unit, name='edit_unit'),
    path('delete_unit/<int:pk>/', views.delete_unit, name='delete_unit'),

    # Landlords
    path('landlords/', views.landlords, name='landlords'),
    path('add_landlord/', views.add_landlord, name='add_landlord'),
    path('edit_landlord/', views.edit_landlord, name='edit_landlord'),
    path('delete_landlord/<int:pk>/', views.delete_landlord, name='delete_landlord'),

    # Tenants
    path('tenants/', views.tenants, name='tenants'),
    path('add_tenant/', views.add_tenant, name='add_tenant'),
    path('edit_tenant/', views.edit_tenant, name='edit_tenant'),
    path('delete_tenant/<int:pk>/', views.delete_tenant, name='delete_tenant'),
    
    # Expenses
    path('expenses/', views.expenses, name='expenses'),
    path('add_expense_profile/', views.add_expense_profile, name='add_expense_profile'),
    path('edit-expense-profile/', views.edit_expense_profile, name='edit_expense_profile'),
    path('delete-expense-profile/<int:pk>/', views.delete_expense_profile, name='delete_expense_profile'),

    # Transactions
    path('upload_statement/', views.upload_bank_statement, name='upload_statement'),
    path('export_parsed_transactions/', views.export_parsed_transactions, name='export_parsed_transactions'),
]
