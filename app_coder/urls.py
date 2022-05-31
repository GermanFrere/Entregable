from django.urls import path

from app_coder import views

urlpatterns = [
    path('', views.index, name='Home'),
    path('employees', views.employees, name='Employees'),
    path('products', views.products, name='Products'),
    
    path('homeworks', views.homeworks, name='Homeworks'),
    path('formHTML', views.form_hmtl),
    path('product-django-forms', views.product_forms_django, name='ProductDjangoForms'),
    path('employee-django-forms', views.employee_forms_django, name='EmployeeDjangoForms'),
    path('homework-django-forms', views.homework_forms_django, name='HomeworkDjangoForms'),
    path('search', views.search, name='Search'),
]
