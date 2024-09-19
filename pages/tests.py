from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    """Test for the home page of django project"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/")

        self.assertEqual(responce.status_code, 200)
