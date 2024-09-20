"""
Caleb Taylor
9/20/2024
CIS218
"""

from django.views.generic import TemplateView

"""classes tell where each page should go"""


class HomePageView(TemplateView):
    template_name = "home.html"


class PreviousProjectsView(TemplateView):
    template_name = "previous_projects.html"


class ContactPageView(TemplateView):
    template_name = "contacts.html"
