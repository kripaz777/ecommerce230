from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from home.models import Category,Slider,Ad,Item


class BaseView(View):
    views = {}

class HomeView(BaseView):
    def get(self,request):
        self.views['categories'] = Category.objects.all()
        self.views['sliders'] = Slider.objects.all()
        self.views['ads1'] = Ad.objects.filter(rank = 1)
        self.views['ads2'] = Ad.objects.filter(rank = 2)
        self.views['ads3'] = Ad.objects.filter(rank = 3)
        self.views['ads4'] = Ad.objects.filter(rank = 4)
        self.views['ads5'] = Ad.objects.filter(rank = 5)
        self.views['ads6'] = Ad.objects.filter(rank = 6)
        self.views['ads7'] = Ad.objects.filter(rank = 7)
        self.views['ads8'] = Ad.objects.filter(rank = 8)

        self.views['items'] = Item.objects.all()
        self.views['new_items'] = Item.objects.filter(label = 'new')
        self.views['hot_items'] = Item.objects.filter(label='hot')
        self.views['sale_items'] = Item.objects.filter(label='sale')
        return render(request,'index.html',self.views)