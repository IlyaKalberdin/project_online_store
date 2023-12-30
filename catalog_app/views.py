from django.shortcuts import render


def home_page(request):
    # Функция возвращает страницу home_page.html
    return render(request, 'catalog_app/home_page.html')


def contact_page(request):
    # Функция возвращает страницу contact_page.html
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')

        print(f'{name}, {number}')
    return render(request, 'catalog_app/contact_page.html')
