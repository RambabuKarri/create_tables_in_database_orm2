from django.db import models

# Create your models here.
class Country(models.Model):
    country_id=models.IntegerField(primary_key=True)
    country_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.country_name

class Capital(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=100)
    country_id=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.cname



