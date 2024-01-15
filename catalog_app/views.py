from django.shortcuts import render
from catalog_app.models import Product, Contact


def home_page(request):
    """Функция возвращает страницу home_page.html и выводит последние
    5 товаров в консоль"""
    last_five_product = Product.objects.all()[:5]

    print(last_five_product)

    context = {'products': Product.objects.all(),
               'title': 'Главная'}

    for product in context['products']:
        product.description = product.description[:100]

    return render(request, 'catalog_app/home_page.html', context)


def product_page(request, product_id):
    """Функция возвращает страницу product_page.html"""
    product_list = Product.objects.filter(id=product_id)
    page_name = product_list[0].name

    context = {'product': product_list,
               'title': page_name}

    return render(request, 'catalog_app/product_page.html', context)


def contact_page(request):
    """Функция возвращает страницу contact_page.html"""
    context = {'contact': Contact.objects.filter(id=1)[0],
               'title': 'Контакты'}

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        print(f'{name}, {number}')

    return render(request, 'catalog_app/contact_page.html', context)
