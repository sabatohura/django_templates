from pyexpat import model
from django.db import models
import uuid
# Create your models here.

class Trainee(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False,serialize=True)
    full_name=models.CharField(max_length=250)
    dob=models.DateField()
    joined_on=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.full_name

   # Trainee.objects.all()
    # Trainee.objects.filter()
    # Trainee.objects.first()
    # Trainee.objects.last()
    # Trainee.objects.latest()
    # Trainee.objects.annotate
    # Trainee.objects.aggregate()
    # Trainee.objects.create()