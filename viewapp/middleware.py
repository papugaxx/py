from . import views


class SectionFallbackMiddleware:
    """
    Якщо користувач відкрив неправильну адресу всередині відомого розділу,
    замість 404 повертаємо головну сторінку цього розділу.

    Приклади:
    /news/heyjude -> /news/
    /management/test -> /management/
    /branches/unknown -> /branches/
    """

    SECTION_VIEWS = {
        "news": views.news,
        "management": views.management,
        "about": views.about,
        "contacts": views.contacts,
        "branches": views.branches,
    }

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code != 404:
            return response

        path = request.path.strip("/")
        if not path:
            return response

        section = path.split("/")[0]
        fallback_view = self.SECTION_VIEWS.get(section)

        if fallback_view is None:
            return response

        return fallback_view(request)
