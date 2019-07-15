from django.db import models

# Create your models here.

class Blood_Request(models.Model):
    Patient_Name = models.CharField(),
    Blood_Group = models.CharField(),
    Number_of_Bag = models.CharField(),
    Hospital = models.CharField(),
    Location = models.CharField(),
    Contact = models.CharField(),

    def __str__(self):
        return self.title


