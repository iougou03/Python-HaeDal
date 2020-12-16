from django.contrib import admin
#사용한 admin theme : https://github.com/sehmaschine/django-grappelli

# Register your models here.
from .models import Haetoos_member

class Haetoos_memberAdmin(admin.ModelAdmin):
    readonly_fields=('haetoos_id','haetoos_ps',)
    fields = ['name','student_id','haetoos_id','haetoos_ps',]
    
admin.site.register(Haetoos_member,Haetoos_memberAdmin)