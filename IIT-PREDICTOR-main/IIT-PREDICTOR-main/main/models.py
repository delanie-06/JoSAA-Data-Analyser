from django.db import models

# Create your models here.
class Record(models.Model):
    Institute = models.CharField(max_length=255)
    Academic_Program_Name = models.CharField(max_length=255)
    Quota = models.CharField(max_length=80)
    Seat_Type = models.CharField(max_length=155)
    Gender = models.CharField(max_length=155 ,null=True)
    Opening_Rank = models.CharField(max_length=80)
    Closing_Rank = models.CharField(max_length=80)
    Year = models.CharField(max_length=155)
    Round = models.IntegerField()
        
    def __str__(self):
        return self.Academic_Program_Name
    