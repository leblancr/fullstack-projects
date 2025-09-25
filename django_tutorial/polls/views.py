from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")

class DetailView(generic.DetailView):
    """
    Shows one question and it's list of choices
    """
    model = Question
    template_name = "polls/detail.html"

    def get_queryset(self):
            """
            Excludes any questions that aren't published yet.
            """
            queryset = Question.objects.filter(pub_date__lte=timezone.now())

            # You can use choice_set here on each Question instance without changing return
            for q in queryset:
                print("q:")
                print(q)
                print("q.choice_set.all():")
                print(q.choice_set.all())
                for choice in q.choice_set.all():
                    print("choice:", end="")
                    print(choice)  # prints each choice_text via __str__
            return queryset

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reverse() gets the urls path from name in urls.py
        # <int:pk>/results/
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
