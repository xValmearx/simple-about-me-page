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

    """test to see if page will load"""

    def test_url_exist_at_current_location(self):
        # gets client form the previous_projects page
        responce = self.client.get("/previous_projects/")

        # test to see if the page is found
        self.assertEqual(responce.status_code, 200)

    """test to see is page name is avalible """

    def test_url_avalible_by_name(self):
        # gets client from the previous_projects page
        responce = self.client.get(reverse("previous_projects"))

        # checks if the name is avalible
        self.assertEqual(responce.status_code, 200)

    """test to see if the page has the correct html"""

    def test_template_name_correct(self):

        # gets client from the previous_projects page
        responce = self.client.get(reverse("previous_projects"))

        # test to see if the previous_projects page is using the correct html
        self.assertTemplateUsed(responce, "previous_projects.html")

    """test to see if the page has the correct header"""

    def test_template_contains(self):

        # gets client form the previous_projejcts page
        response = self.client.get(reverse("previous_projects"))

        # test to see if the page containes the proper header
        self.assertContains(response, "<h2>Previous projects I have worked on</h2>")


"""test for contacts page"""


class ContactsTest(SimpleTestCase):
    """Test for the home page of django project"""

    def test_url_exist_at_current_location(self):

        # creates client form the contacts page
        responce = self.client.get("/contacts/")

        # test to see if page will load
        self.assertEqual(responce.status_code, 200)

    """test to see is page name is avalible """

    def test_url_avalible_by_name(self):

        # creates client from the contacts page
        responce = self.client.get(reverse("contacts"))

        # test to see if the page has the correct name
        self.assertEqual(responce.status_code, 200)

    """test to see if the page has the correct html"""

    def test_template_name_correct(self):
        # creates client from the contacts page
        responce = self.client.get(reverse("contacts"))

        # test to see if the page has the correct html
        self.assertTemplateUsed(responce, "contacts.html")

    """test to see if the page has the correct header"""

    def test_template_contains(self):
        # gets client form the contacts page
        response = self.client.get(reverse("contacts"))

        # test to see if the page has the propper header
        self.assertContains(response, "<h1>Contact Info</h1>")
