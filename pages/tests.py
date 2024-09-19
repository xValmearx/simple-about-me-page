from django.test import SimpleTestCase


class HomePageTest(SimpleTestCase):
    """Test for the home page of django project"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/")

        self.assertEqual(responce.status_code, 200)


class PreviousProjectsTest(SimpleTestCase):
    """Test for the home page of django project"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/previous_projects/")

        self.assertEqual(responce.status_code, 200)


class ContactsTest(SimpleTestCase):
    """Test for the home page of django project"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/contacts/")

        self.assertEqual(responce.status_code, 200)
