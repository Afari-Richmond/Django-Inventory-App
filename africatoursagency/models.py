from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()


    # This is a string representation of the Tours
    def __str__(self):
        return (f"ID: {self.id}: From {self.origin_country} To {self.destination_country}, {self.number_of_nights} nights cost ${self.price}")
