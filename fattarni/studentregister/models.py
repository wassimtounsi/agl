from django.db import models

class students(models.Model):
    fullname = models.CharField(max_length=50)
    email =models.EmailField()
    password = models.CharField()
class menu(models.Model):
    menu=models.TextField()
    submission_date = models.DateTimeField(auto_now_add=True)