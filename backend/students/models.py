from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    age=models.IntegerField()
    department=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    #model -Database structure
    #views -Application Logic
    #Template -HTML user Interface
    # URL -connects the browser request to views

    # these are the orm  operations
    #retrive the student by name:
    # retrive only the email 
    # count total students
    # update the students's age
    #ctrl+/