import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # return whatever string you want
    def __str__(self):
        return self.question_text

    # Currently within one day
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    #  each Choice object has only one choice text.
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # the question obj this goes with
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    choice_text = models.CharField(max_length=200) #
    image_url = models.CharField(max_length=500, blank=True, null=True)  # path to image
    image_size = models.CharField(
        max_length=20,
        choices=[("inline", "Inline Icon"), ("small", "Small"), ("medium", "Medium"), ("large", "Large")],
        default="medium",
    )
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
