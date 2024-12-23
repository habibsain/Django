from django.db import models

# Create your models here.
class Question(models.Model):
    q_text = models.CharField(max_length=200)
    enquiryy_date = models.DateTimeField("date of enquiry")

class Choice(models.Model):
    Question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)