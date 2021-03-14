from django.contrib import admin
from csvexport.actions import csvexport
from .models import *
# Register your models here.
class item(admin.ModelAdmin):
    list_display = ("title","price","category","brand","status","label","image")
    search_fields = ["title","description"]
    list_filter = ("status","label","category")
    list_per_page = 20
    actions = [csvexport]

admin.site.register(Item,item)

class category(admin.ModelAdmin):
    list_display = ("name","slug","image")
    search_fields = ["name"]

    list_per_page = 20
admin.site.register(Category,category)

admin.site.register(Slider)
admin.site.register(Ad)
admin.site.register(Brand)

admin.site.register(Cart)