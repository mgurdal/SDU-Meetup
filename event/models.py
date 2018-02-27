from django.db import models
from hvad.models import TranslatableModel, TranslatedFields
# Create your models here.
class Member(models.Model):
    """docstring for Member."""
    student_no= models.IntegerField()
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    registeration_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    # translations = TranslatedFields(
    #     title = models.CharField(max_length=250)
    # )
    def __str__(self):
        return self.name
