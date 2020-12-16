from django.db import models

# Create your models here.
class Haetoos_member(models.Model): #Model을 상속받음
    #이름,id, password
    name = models.CharField(max_length=30)
    haetoos_id = models.CharField(max_length=30)
    haetoos_ps = models.CharField(max_length=30)
    #학번
    student_id = models.IntegerField() 
    
    def __str__(self):
        return self.name