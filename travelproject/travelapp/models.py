from django.db import models
class Place(models.Model):
      name=models.CharField(max_length=250)
      image=models.ImageField(upload_to="pics")
      desc=models.TextField()
class Guides(models.Model):
      name=models.CharField(max_length=250)
      img=models.ImageField(upload_to="pics")
      desg=models.TextField()
      def __str__(self):
            return self.name