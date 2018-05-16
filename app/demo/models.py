from django.db import models


class House(models.Model):
    bed = models.SmallIntegerField('Bedrooms', choices=((x, str(x)) for x in range(1, 7)))
    bath = models.SmallIntegerField('Bathrooms', choices=((x, str(x)) for x in range(1, 5)))
    heat = models.CharField('Heating', max_length=4,
                            choices=(("NG", "Natural Gas"), ("Elec", "Electric"), ("Wood", "Wood")))
    garage = models.BooleanField("Garage?")

    def __str__(self):
        return "{} bedroom / {} bathroom".format(self.bed, self.bath)
