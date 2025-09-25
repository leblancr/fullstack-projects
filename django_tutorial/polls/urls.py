from django.urls import path

from . import views

"""
first arg = route, path after http://127.0.0.1:8000/polls/
route is a string that contains a URL pattern.
When processing a request, Django starts at the first pattern in urlpatterns
and makes its way down the list, comparing the requested URL against each pattern until
it finds one that matches.
Patterns don’t search GET and POST parameters, or the domain name.
For example, in a request to https://www.example.com/myapp/, the URLconf will look for myapp/.
In a request to https://www.example.com/myapp/?page=3, the URLconf will also look for myapp/.

second arg = file.function to run (view) When Django finds a matching pattern,
it calls the specified view function with an HttpRequest object as the first argument and
any “captured” values from the route as keyword arguments. a view is a function.

Naming your URL lets you refer to it unambiguously from elsewhere in Django, especially from within templates.
This powerful feature allows global changes to the URL patterns of your project while only touching a single file.
"""

app_name = "polls"

# path to function map
# 1st arg = everything after http://127.0.0.1:8000/polls/
# 2nd arg = function in polls/views.py
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
