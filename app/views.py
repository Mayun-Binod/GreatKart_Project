from django.shortcuts import render,get_object_or_404
from app.models import Product,Customer,Cart,OrderPlaced
from django.views import View

class ProductView(View):
    def get(self, request):
        # Filter products by category
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')

        # Prepare context data
        context = {
            'topwears': topwear,
            'bottomwears': bottomwear,
            'laptops': laptop,
            'mobiles': mobile,
        }

        # Render the template with context
        return render(request, 'app/home.html', context)

class ProductDetail(View):
    def get(self, request, product_id):
        # Fetch the product by ID or return a 404 error if not found
        product = get_object_or_404(Product, id=product_id)
        
        # Prepare context data
        context = {
            "products": product  # Use "product" instead of "products"
        }
        
        # Render the template with context
        return render(request, 'app/productdetail.html', context)

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
 if data==None:
   mobile=Product.objects.filter(category="M")
 elif data=="Redmi" or data=="Samsung" or data=="Iphone":
   mobile=Product.objects.filter(category="M").filter(brand=data)
 elif data=="Below":
   mobile=Product.objects.filter(category="M").filter(discounted_price__lt=10000)
 elif data=="Above":
   mobile=Product.objects.filter(category="M").filter(discounted_price__gt=10000)
 return render(request, 'app/mobile.html',{'mobiles':mobile})

def laptop(request,data=None):
 if data==None:
   laptop=Product.objects.filter(category="L")
 elif data=="Dell" or data=="Mac" or data=="Asur":
   laptop=Product.objects.filter(category="L").filter(brand=data)
 elif data=="Below":
   laptop=Product.objects.filter(category="L").filter(discounted_price__lt=15000)
 elif data=="Above":
   laptop=Product.objects.filter(category="L").filter(discounted_price__gt=15000)
 return render(request, 'app/laptop.html',{'laptops':laptop})


def topwear(request,data=None):
 if data==None:
   topwear=Product.objects.filter(category="TW")
 elif data=="Park" or data=="Polo":
   topwear=Product.objects.filter(category="TW").filter(brand=data)
 elif data=="Below":
   topwear=Product.objects.filter(category="TW").filter(discounted_price__lt=1000)
 elif data=="Above":
   topwear=Product.objects.filter(category="TW").filter(discounted_price__gt=1000)
 return render(request, 'app/topwear.html',{'topwears':topwear})


def bottomwear(request,data=None):
 if data==None:
   bottomwear=Product.objects.filter(category="BW")
 elif data=="Lee" or data=="Spykar":
   bottomwear=Product.objects.filter(category="BW").filter(brand=data)
 elif data=="Below":
   bottomwear=Product.objects.filter(category="BW").filter(discounted_price__lt=400)
 elif data=="Above":
   bottomwear=Product.objects.filter(category="BW").filter(discounted_price__gt=400)
 return render(request, 'app/bottomwear.html',{'bottomwears':bottomwear})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
