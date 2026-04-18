from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>Головна</h1><p>Ласкаво просимо на сайт компанії</p>")


def news(request):
    return HttpResponse("<h1>Новини</h1><p>Тут будуть новини компанії</p>")


def management(request):
    return HttpResponse("<h1>Керівництво компанії</h1><p>Інформація про керівництво компанії</p>")


def about(request):
    return HttpResponse("<h1>Про компанію</h1><p>Інформація про компанію</p>")


def contacts(request):
    return HttpResponse("<h1>Контакти</h1><p>Контактна інформація компанії</p>")