from django.db import models
from datetime import datetime
from membership.models import BourgeoisMember

class Freeboard(models.Model):
    f_no = models.AutoField(primary_key=True)
   
    member = models.ForeignKey(BourgeoisMember,on_delete=models.DO_NOTHING,null=True)
    f_title = models.CharField(max_length=1000)
    f_content = models.TextField()
    f_group = models.IntegerField(default=0)
    f_step = models.IntegerField(default=0)
    f_indent = models.IntegerField(default=0)
    f_hit = models.IntegerField(default=1)
    f_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    f_updatedate = models.DateTimeField(default=datetime.now(),blank=True)
    f_file = models.ImageField(blank=True)
    
    def __str__(self):
        return self.f_title