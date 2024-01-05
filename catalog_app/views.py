from django.shortcuts import render
from catalog_app.models import Product, Contact


def home_page(request):
    """Функция возвращает страницу home_page.html и выводит последние
    5 товаров в консоль"""
    last_five_product = Product.objects.all()[:5]

    print(last_five_product)

    return render(request, 'catalog_app/home_page.html')


def contact_page(request):
    """Функция возвращает страницу contact_page.html"""
    contact = {'contact': Contact.objects.filter(id=1)[0]}

    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        print(f'{name}, {number}')

    return render(request, 'catalog_app/contact_page.html', contact)
