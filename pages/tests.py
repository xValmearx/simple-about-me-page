"""
Caleb Taylor
9/20/2024
CIS218
"""

from django.test import SimpleTestCase
from django.urls import reverse


"""Tests for the home page """


class HomePageTest(SimpleTestCase):
    """Tests to see of the page will load"""

    def test_url_exist_at_current_location(self):

        # create client form the rout page, aka home page
        responce = self.client.get("/")

        # checks if the page will load
        self.assertEqual(responce.status_code, 200)

    """test to see is page name is avalible """

    def test_url_avalible_by_name(self):

        # creates client of the home.html page
        responce = self.client.get(reverse("home"))

        # checks if the page name is avalible
        self.assertEqual(responce.status_code, 200)

        """Test to see if the correct html page is being used"""

    def test_template_name_correct(self):
        # creates client from home page
        response = self.client.get(reverse("home"))

        # checks if the home page is using home.html
        self.assertTemplateUsed(response, "home.html")

    """Test for proper header in html file"""

    def test_template_contains(self):

        # creates client from home page
        response = self.client.get(reverse("home"))

        # checks if homepage header matches inserted header
        self.assertContains(response, "<h2>About Myself</h2>")


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

    def test_template_name_correct(self):
        responce = self.client.get(reverse("previous_projects"))

        self.assertTemplateUsed(responce, "previous_projects.html")

    def test_template_contains(self):
        response = self.client.get(reverse("previous_projects"))

        self.assertContains(response, "<h2>Previous projects I have worked on</h2>")


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

    def test_template_name_correct(self):
        responce = self.client.get(reverse("contacts"))

        self.assertTemplateUsed(responce, "contacts.html")

    def test_template_contains(self):
        response = self.client.get(reverse("contacts"))

        self.assertContains(response, "<h1>Contact Info</h1>")
