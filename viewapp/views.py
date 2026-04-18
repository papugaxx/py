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


def branches(request):
    return HttpResponse("""
        <h1>Філії</h1>
        <p>Наші філії:</p>
        <ul>
            <li>London</li>
            <li>Paris</li>
            <li>Odessa</li>
        </ul>
    """)


def branch_detail(request, city):
    branches_info = {
        "London": "Філія у Лондоні. Адреса: Baker Street, 221B.",
        "Paris": "Філія у Парижі. Адреса: Avenue des Champs-Élysées.",
        "Odessa": "Філія в Одесі. Адреса: Дерибасівська, 1.",
    }

    if city in branches_info:
        return HttpResponse(f"<h1>{city}</h1><p>{branches_info[city]}</p>")

    return HttpResponse("<h1>Філія не знайдена</h1>", status=404)