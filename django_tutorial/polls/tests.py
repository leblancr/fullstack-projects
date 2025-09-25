import datetime
import inspect

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)  # ORM handles args __init__() in Models
        self.assertIs(future_question.was_published_recently(), False)  # should return false


    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)


    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

def create_question(question_text, days):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    print(f"Running {inspect.currentframe().f_code.co_name} with {question_text}")
    time = timezone.now() + datetime.timedelta(days=days)
    question = Question.objects.create(question_text=question_text, pub_date=time)
    print('question:', question)

    # Assert that the object is saved correctly
    assert Question.objects.filter(id=question.id).exists(), f"Question with ID {question.id} not found in database"
    assert question.question_text == question_text, f"Expected question_text '{question_text}', got '{question.question_text}'"

    # Retrieve all Question objects
    questions = Question.objects.all()
    print('questions:', questions)

    # Print details of each question
    for question in questions:
        print(f"Question ID: {question.id}, Question Text: {question.question_text}, Pub Date: {question.pub_date}")

    return question

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        response = self.client.get(reverse("polls:index"))  # reverse return url for name
        print('response:', response.content)
        print('response.context["latest_question_list"]:', response.context["latest_question_list"])
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_past_question(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        question = create_question(question_text="Past question.", days=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        question = create_question(question_text="Past question.", days=-30)
        create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question],
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        print(f"Running {inspect.currentframe().f_code.co_name}")
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [question2, question1],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_question(question_text="Future question.", days=5)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_question(question_text="Past Question.", days=-5)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)
