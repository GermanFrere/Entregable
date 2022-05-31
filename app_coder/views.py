from django.shortcuts import render
from django.db.models import Q

from app_coder.models import Product, Employee, Homework
from app_coder.forms import ProductForm, EmployeeForm, HomeworkForm


def index(request):
    return render(request, "app_coder/home.html")


def employees(request):
    employees = Employee.objects.all()

    context_dict = {
        'employees': employees
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/employees.html"
    )


def products(request):
    products = Product.objects.all()

    context_dict = {
        'products': products
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/products.html"
    )





def homeworks(request):
    homeworks = Homework.objects.all()

    context_dict = {
        'homeworks': homeworks
    }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/homeworks.html"
    )


def form_hmtl(request):

    if request.method == 'POST':
        product = Product(name=request.POST['name'], code=request.POST['code'])
        product.save()

        products = Product.objects.all()
        context_dict = {
            'products': products
        }

        return render(
            request=request,
            context=context_dict,
            template_name="app_coder/products.html"
        )

    return render(
        request=request,
        template_name='app_coder/formHTML.html'
    )


def product_forms_django(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            data = product_form.cleaned_data
            product = Product(name=data['name'], code=data['code'])
            product.save()

            products = Product.objects.all()
            context_dict = {
                'products': products
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/products.html"
            )

    product_form = ProductForm(request.POST)
    context_dict = {
        'product_form': product_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/product_django_forms.html'
    )


def employee_forms_django(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST)
        if employee_form.is_valid():
            data = employee_form.cleaned_data
            employee = Employee(
                name=data['name'],
                last_name=data['last_name'],
                email=data['email'],
                profession=data['profession'],
            )
            employee.save()

            employees = Employee.objects.all()
            context_dict = {
                'employees': employees
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/employees.html"
            )

    employee_form = EmployeeForm(request.POST)
    context_dict = {
        'employee_form': employee_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/employee_django_forms.html'
    )


def homework_forms_django(request):
    if request.method == 'POST':
        homework_form = HomeworkForm(request.POST)
        if homework_form.is_valid():
            data = homework_form.cleaned_data
            homework = Homework(
                name=data['name'],
                due_date=data['due_date'],
                is_delivered=data['is_delivered'],
            )
            homework.save()

            homeworks = Homework.objects.all()
            context_dict = {
                'homeworks': homeworks
            }
            return render(
                request=request,
                context=context_dict,
                template_name="app_coder/homeworks.html"
            )

    homework_form = HomeworkForm(request.POST)
    context_dict = {
        'homework_form': homework_form
    }
    return render(
        request=request,
        context=context_dict,
        template_name='app_coder/homework_django_forms.html'
    )


def search(request):
    context_dict = dict()
    if request.GET['text_search']:
        search_param = request.GET['text_search']
        products = Product.objects.filter(name__contains=search_param)
        context_dict = {
            'products': products
        }
    elif request.GET['code_search']:
        search_param = request.GET['code_search']
        products = Products.objects.filter(code__contains=search_param)
        context_dict = {
            'products': products
        }
    elif request.GET['all_search']:
        search_param = request.GET['all_search']
        query = Q(name__contains=search_param)
        query.add(Q(code__contains=search_param), Q.OR)
        products = Product.objects.filter(query)
        context_dict = {
            'products': products
        }

    return render(
        request=request,
        context=context_dict,
        template_name="app_coder/home.html",
    )
