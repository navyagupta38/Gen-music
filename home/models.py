# MODELS:- jo ki hmare database ko define krti h
from django.db import models

# Create your models here.
class Contact(models.Model):    #contact:- a type of databse in a table (like excelsheet)
    name = models.CharField(max_length=122) # :- these are like cols of excel sheet
    email= models.CharField(max_length=122)   # :- these are like cols of excel sheet
    phone=models.CharField(max_length=12)    # :- these are like cols of excel sheet
    desc = models.TextField()     # :- these are like cols of excel sheet
    date=models.DateField()      # :- these are like cols of excel sheet
# python manage.py makemigration :- django ko y btaaega ki maine kuch changes kiye h maine un changes ke file bnaado

# to detect the changes
# i. :- to register our models

    def __str__(self):
        return self.name