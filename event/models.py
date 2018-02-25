from django.db import models

# Create your models here.
class Member(models.Model):
    """docstring for Member."""
    student_no= models.PositiveIntegerField()
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    registeration_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name
