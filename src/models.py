from django.db import models

class Store(models.Model):
    title = models.CharField(max_length=20)
    goods = models.CharField(max_length=255)
    vidio_devais = models.CharField(max_length=255)
    npk = models.CharField(max_length=255)
    phones = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title   
    
class Photos(models.Model):
    title = models.CharField(max_length=255)
    photob = models.ImageField()

    def __str__(self) -> str:
        return self.title
