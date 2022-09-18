from datetime import datetime
from django.db import models

class BourgeoisMember(models.Model):
    ID = models.CharField(max_length=100, primary_key=True)
    PW = models.CharField(max_length=100)
    NAME = models.CharField(max_length=100)
    AGE = models.IntegerField(default=0)
    GENDER = models.CharField(max_length=16)
    LEGION = models.CharField(max_length=50)
    CuriousLEGION = models.CharField(max_length=50)
    CuriousSECTOR = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ID