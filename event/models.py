from django.db import models
# Create your models here.


class Member(models.Model):
    """docstring for Member."""
    student_no = models.IntegerField()
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    university_branch = models.CharField(max_length=250, default='Default') #Okudugu bolum.
    title = models.CharField(max_length=100) #Unvan
    selected_education = models.CharField(max_length=250, default='Default') #Sectigi egitim.
    registeration_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
