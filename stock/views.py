from django.db.models.base import Model
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render,redirect
from django.views.generic import TemplateView,CreateView,View,FormView,UpdateView,DeleteView
from.models import Admin, Product
from.forms import Adminform,loginForm,CatergoryForm,productForm,UpdateproductForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q


# Create your views here.
class SuperUserRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and User.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)


class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)

class IndexView(AdminRequiredMixin,TemplateView):
    
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['product']=Product.objects.all().order_by('-id')
        return context

class addproductView(AdminRequiredMixin,CreateView):
    
    form_class = productForm
    template_name ='addproduct.html'
    success_url=reverse_lazy('home')
    
    

class updateproductView(AdminRequiredMixin,UpdateView):
    
    form_class = UpdateproductForm
    template_name ='updateproduct.html'
    queryset = Product.objects.all()
    success_url=reverse_lazy('home')
   
class deleteView(DeleteView):
    queryset = Product.objects.all()
    context_object_name='product'
    template_name ='delete.html'
    success_url =reverse_lazy('home')
    

class AddCatergoryView(AdminRequiredMixin,CreateView):
    
    form_class = CatergoryForm
    template_name ='addcatergory.html'
    success_url=reverse_lazy('home')

class ProductDetailsView(AdminRequiredMixin,TemplateView):
    template_name= 'details.html'
    def get_context_data(self, **kwargs): 
        contex = super().get_context_data(**kwargs)
        url_slug =self.kwargs['slug']
        product=Product.objects.get(slug=url_slug)
        
        contex['product_details']=product
        return contex
    

class AdminRegisterView(AdminRequiredMixin,CreateView):
    form_class = Adminform
    template_name ='admin/admin_register.html'
    success_url= reverse_lazy('home')
## Admin form eken auth User ekata onetoone field walin add karana method eka
    def form_valid(self, form):
        
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = User.objects.create_user(username,email,password)
        form.instance.user= user
        login(self.request,user)
        return super().form_valid(form)

class AdminloginView(FormView):

    success_url= reverse_lazy("home")
    form_class = loginForm
    template_name ='admin/admin_login.html'
    
## form eken authenticate karala user innawada balana method eka
    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

class AdminlogoutView(AdminRequiredMixin,View):
    def get(self,request):
        logout(request)
        return redirect(reverse_lazy('home'))

class Search_kew_word(TemplateView):
    template_name='search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        kw = self.request.GET['keyword']
        results = Product.objects.filter(Q(product_name__icontains=kw)|Q(discriptions__icontains=kw))
        context['result']=results
        return context