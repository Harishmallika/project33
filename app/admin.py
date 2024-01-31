from django.contrib import admin

# Register your models here.

from app.models  import *


class CustomizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']






admin.site.register(Topic)

admin.site.register(Webpage,CustomizeWebpage)

admin.site.register(AccessRecord)


