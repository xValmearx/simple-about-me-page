from django.urls import path

from .views import HomePageView, PreviousProjectsView, ContactPageView

urlpatterns = [
    path("previous_projects/", PreviousProjectsView.as_view(), name="previous_projects"),
    path("", HomePageView.as_view(), name="home"),
    path("/contacts", ContactPageView.as_view(), name="contacts"),
]
