from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    author = models.CharField(max_length=200, verbose_name="Author")
    published_date = models.DateField(verbose_name="Published Date")

    def __str__(self):
        return self.name