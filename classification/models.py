from django.db import models

# Create your models here.


class Prediction(models.Model):

    image = models.ImageField(verbose_name="Image",null=False, blank=False, upload_to="predictedImages/")
    prediction = models.CharField(max_length=254)
    def __str__(self):
        return (self.image, self.prediction)
    
