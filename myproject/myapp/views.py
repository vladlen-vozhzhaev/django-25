import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(req):
    return render(req, "index.html", context={"title": "Главная страница"})

def about(req):
    return render(req, "about.html")

def contactUs(req):
    return render(req, "contact-us.html")

def products(req):
    products = [
        {
            "name": "Монитор DEXP DF22N1 серебристый",
            "price": 7499,
            "img": "https://c.dns-shop.ru/thumb/st4/fit/0/0/5e3b6e5a2d2f34285cff9239ea17890e/d870f12185a7312b4ac4fc2a60cf4bd3d96df0a6703914835d46ff07d2841470.jpg.webp"
        },
        {
            "name": "Усилитель интернет-сигнала РЭМО BAS-2362",
            "price": 10799,
            "img": "https://c.dns-shop.ru/thumb/st4/fit/wm/0/0/44352d401e448dff87ec328bdcbd6290/cf50561def52c5ccaa3cc08c272e73aed60298e23e6aa5284ce6dd00126a807b.jpg.webp"
        },
        {
            "name": "Клавиатура проводная Razer Ornata V3 X",
            "price": 3999,
            "img": "https://c.dns-shop.ru/thumb/st4/fit/0/0/b36895b4b897772a3de6f3e0e4dec88d/82f59d5d15089f142d21d9b53b6d41de67fcd07acf94e71e7fd811bc2e7fed8d.jpg.webp"
        }
    ]
    return render(req, "products.html", context={"products": products})

def game(request):
    num1 = random.randint(0, 3)
    num2 = random.randint(0, 3)
    num3 = random.randint(0, 3)
    if num1 == num2 == num3:
        response = f"Победа, все 3 числа равны! Числа: {num1}, {num2}, {num3}"
    else:
        response = f"Повезет в следующий раз! Числа: {num1}, {num2}, {num3}"
    return HttpResponse(response)

def get_phrase1(req):
    return HttpResponse("Первая фраза")

def get_phrase2(req):
    return HttpResponse("Вторая фраза")
def contact(req):
    print(req.POST.get("name"))
    print(req.POST.get("email"))
    print(req.POST.get("msg"))
    return HttpResponse("Форма успешно отправлена!")