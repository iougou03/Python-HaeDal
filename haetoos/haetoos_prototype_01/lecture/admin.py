from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.utils import get_attachment_model

from .models import LectureList

# Register your models here.
# class LectureListAdmin(admin.ModelAdmin):
    # fields = ['youtube_url',]

class LectureListAdmin(SummernoteModelAdmin):
    summernote_fields=('content',)

admin.site.register(LectureList,LectureListAdmin)
admin.site.unregister(get_attachment_model())




