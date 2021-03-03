from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic.base import View
from django.contrib import messages,auth
from django.contrib.auth.models import User
from home.models import Category,Slider,Ad,Item,Brand


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

class ProductDetailView(BaseView):
    def get(self, request,slug):
        category = Item.objects.get(slug = slug).category
        self.views['detail_item'] = Item.objects.filter(slug = slug)
        self.views['categories'] = Category.objects.all()
        self.views['brands'] = Brand.objects.all()
        self.views['related_item'] = Item.objects.filter(category=category)
        return render(request,'product-detail.html',self.views)

class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query',None)
        if not query:
            return redirect("/")
        self.views['search_query'] = Item.objects.filter(

            description__icontains =query
        )
        self.views['searched_for'] = query
        return render(request,'search.html',self.views)


class CategoryView(BaseView):
    def get(self,request,slug):
        cat = Category.objects.get(slug=slug).id
        self.views['category_items'] = Item.objects.filter(category = cat)

        return render(request,'category.html',self.views)
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,'The username is already used.')
                return redirect('home:signup')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'The email is already used.')
                return redirect('home:signup')
            else:
                data = User.objects.create_user(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    email = email,
                    password = password
                )
                data.save()
                messages.error(request, 'You are signed up.')
                return redirect('home:signup')
        else:
            messages.error(request, 'Password doest not match to each other.')
            return redirect('home:signup')

    return render(request,'signup.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.error(request,'Username and password do not match.')
            return redirect('home:login')

    return render(request,'signin.html')