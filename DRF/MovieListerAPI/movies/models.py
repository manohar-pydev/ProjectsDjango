from django.db import models

# Create your models here.
class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    image = models.ImageField(upload_to = 'Images/',default='Images/None/Noimg.jpg')
    movie_type = models.CharField(max_length=200,default="Action")
    
    def __str__(self):
        return self.name