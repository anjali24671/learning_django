# helps us build database models. Which will model the characteristics of the data in our database
from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField() # holds textual data

    def __str__(self):
        '''To not show Post object. It will display the first 50 chr of textField'''
        return self.text[:50]