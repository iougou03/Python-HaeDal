from django.db import models  

# Create your models here.
class HaedalMember(models.Model):
    name = models.CharField(max_length=30, verbose_name="이름")
    student_id = models.IntegerField(verbose_name="학번") 
    phone_number = models.IntegerField(default=0, verbose_name="전화번호",blank=True)
    haetoos_id = models.CharField(max_length=50, verbose_name="ID",blank=True)
    haetoos_ps = models.CharField(max_length=50,verbose_name="비밀번호",blank=True)    
    email = models.EmailField(verbose_name="E-mail",blank=True)
    
    def __str__(self):
        return self.name
