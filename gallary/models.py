from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Photo(models.Model):
    tags = (('CAR', 'CAR'), ('Wildlife', 'Wildlife'), ('Potrait', 'Potrait'))
    name = MultiSelectField(choices=tags)
    image = models.ImageField()
