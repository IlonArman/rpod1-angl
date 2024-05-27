from django.db import models

from datetime import datetime

class Curs(models. Model):

    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description")
    language_lvl = models.CharField(max_length=100, default='beginner') 
    learn_time = models.CharField("Learn time", max_length=255)
    learn_price = models.CharField("Learn price", max_length=255)

    class Meta:

        verbose_name = "Curs"

        verbose_name_plural = "Cursy"

    def __str__(self):

        return self.title
