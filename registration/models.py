from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user=models.OneToOneField(User)
    UNDERAGE=0
    EARLY_CAREER=1
    MID_CAREER=2
    END_CAREER=3
    RETIREMENT =4
    AGE_GROUPS = (
        (UNDERAGE, 'Under 18'),
        (EARLY_CAREER, '18-25'),
        (MID_CAREER,'25-40'),
        (END_CAREER, '40-60'),
        (RETIREMENT,'Over 60')
    )
    sittingDaily = models.IntegerField("How much time would you like to spend sitting daily", blank=True)
    walkingDaily = models.IntegerField("How much time would you like to spend walking daily", blank=True)
    sittingWeekly = models.IntegerField("How much time would you like to spend sitting weekly", blank=True)
    walkingWeekly = models.IntegerField("How much time would you like to spend walking weekly", blank=True)
   
    ageGroup = models.IntegerField("What age group do you belong to", max_length=25, choices = AGE_GROUPS, default=EARLY_CAREER)
    sex = models.BooleanField()
    workoutFreq = models.IntegerField("How often do you workout per week")
    sittingTime = models.IntegerField("Set a max time you would like to sit")
    mode = models.IntegerField()
    participant = models.BooleanField("Would you like to participate in our study")
    joined = models.DateTimeField("Date joined", auto_now_add = True)
    sittingEstimate = models.IntegerField("How much time do you think you spend sitting daily",blank=False)
    walkingEstimate = models.IntegerField("How much time do you think you spend walking daily",blank=False)

    def __unicode__(self):
        return self.user.username
