from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from PIL import Image
import os
# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10,choices=(('Male','Male'),("Female","Female")))
    student_id = models.CharField(max_length=10, null=True, blank=True)

class ImageModel(models.Model):
    original_image = models.ImageField(upload_to='images')
    thumbnail_small = models.ImageField(upload_to='images/thumbnails',null=True, blank=True)
    thumbnail_medium = models.ImageField(upload_to='images/thumbnails',null=True, blank=True)
    thumbnail_large = models.ImageField(upload_to='images/thumbnails',null=True, blank=True)

@receiver(post_save, sender=ImageModel)
def create_thumbnails(sender,instance, created, **kwargs):
    if created:
        sizes ={
        "thumbnail_small": (100,100),
        "thumbnail_medium":(300,300),
        "thumbnail_large":(600,600)
        }
        for field, size in sizes.items():
            img = Image.open(instance.original_image.path)
            img.thumbnail(size,Image.Resampling.LANCZOS)
            thumb_name, thumb_extension = os.path.split(instance.original_image.name)
            thumb_extension = thumb_extension.lower()
            thumb_filename = f"{thumb_name}_{size[0]}x{size[1]}{thumb_extension}"
            thumb_path =  f"thumbnails/{thumb_filename}"
            print(thumb_path)
            img.save(thumb_path)
            setattr(instance,field,thumb_path)









@receiver(post_save, sender = Student)
def save_student(sender, instance,created, **kwargs):
    print(sender, instance)
    if created:
        instance.student_id = f"STU-000{instance.id}"
        instance.save()
    print(" student object created")