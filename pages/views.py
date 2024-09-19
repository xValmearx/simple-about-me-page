from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class PreviousProjectsView(TemplateView):
    template_name = "previous_projects.html"


class ContactPageView(TemplateView):
    template_name = "contacts.html"
