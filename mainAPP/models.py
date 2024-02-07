from django.db import models

class Togri_soz(models.Model):
    soz=models.CharField(max_length=255)


    def __str__(self):
        return self.soz

class Notogri_soz(models.Model):
    soz=models.CharField(max_length=255)
    t_soz=models.ForeignKey(Togri_soz, on_delete=models.CASCADE)

    def __str__(self):
        return self.soz