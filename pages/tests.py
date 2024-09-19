from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTest(SimpleTestCase):
    """Test to see if page is found"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/")

        self.assertEqual(responce.status_code, 200)

    """test to see is page name is avalible """

    def test_url_avalible_by_name(self):
        responce = self.client.get(reverse("home"))

        self.assertEqual(responce.status_code, 200)


"""test for previous projects page"""


class PreviousProjectsTest(SimpleTestCase):
    """test to see if page is found"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/previous_projects/")

        self.assertEqual(responce.status_code, 200)

    """test to see is page name is avalible """

    def test_url_avalible_by_name(self):
        responce = self.client.get(reverse("previous_projects"))

        self.assertEqual(responce.status_code, 200)


"""test for contacts page"""


class ContactsTest(SimpleTestCase):
    """Test for the home page of django project"""

    def test_url_exist_at_current_location(self):
        responce = self.client.get("/contacts/")

        self.assertEqual(responce.status_code, 200)

    """test to see is page name is avalible """

    def test_url_avalible_by_name(self):
        responce = self.client.get(reverse("contacts"))

        self.assertEqual(responce.status_code, 200)
