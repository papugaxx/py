from django.test import TestCase


class SectionFallbackMiddlewareTests(TestCase):
    def test_invalid_news_subpath_returns_news_page(self):
        response = self.client.get('/news/heyjude/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Новини')

    def test_invalid_management_subpath_returns_management_page(self):
        response = self.client.get('/management/test/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Керівництво компанії')

    def test_invalid_branch_returns_branches_page(self):
        response = self.client.get('/branches/heyjude/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Філії')

    def test_valid_branch_still_works(self):
        response = self.client.get('/branches/London/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Філія у Лондоні')

    def test_unknown_top_level_url_still_returns_404(self):
        response = self.client.get('/totally-unknown-page/')
        self.assertEqual(response.status_code, 404)
