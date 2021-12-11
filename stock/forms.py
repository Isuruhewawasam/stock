from django import forms
from .models import *
from django.contrib.auth.models import User

class Adminform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Admin
        fields = ["username","password","email","mobile"]

        widgets={
            'mobile':forms.TextInput(attrs={'class':'form-control'}),
            
        }
## user kalin register welada kiyala validate karana vidiya
    def clean_username(self):
        uname = self.cleaned_data.get('username')
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError('user already exists')
        return uname

class loginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class CatergoryForm(forms.ModelForm):
    class Meta:
        model = Catogory
        fields = '__all__'

        widgets ={

            'cat_name':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            

        }

class productForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['product_name','slug','product_cat','product_Created_by','image','product_price','suppler_price','sale_price','stock_contity','discriptions','worrenty','return_policy']

       
        widgets ={

            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'product_cat':forms.Select(attrs={'class':'form-control'}),
            'product_Created_by':forms.Select(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'product_price':forms.TextInput(attrs={'class':'form-control'}),
            'suppler_price':forms.TextInput(attrs={'class':'form-control'}),
            'sale_price':forms.TextInput(attrs={'class':'form-control'}),
            'stock_contity':forms.TextInput(attrs={'class':'form-control'}),
            'discriptions':forms.Textarea(attrs={'class':'form-control'}),
            'worrenty':forms.TextInput(attrs={'class':'form-control'}),
            'return_policy':forms.TextInput(attrs={'class':'form-control'}),
            
            

        }

class UpdateproductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['product_name','slug','product_cat','image','product_price','suppler_price','sale_price','stock_contity','discriptions','worrenty','return_policy']

       
        widgets ={

            'product_name':forms.TextInput(attrs={'class':'form-control'}),
            'slug':forms.TextInput(attrs={'class':'form-control'}),
            'product_cat':forms.Select(attrs={'class':'form-control'}),
            
            'image':forms.FileInput(attrs={'class':'form-control'}),
            'product_price':forms.TextInput(attrs={'class':'form-control'}),
            'suppler_price':forms.TextInput(attrs={'class':'form-control'}),
            'sale_price':forms.TextInput(attrs={'class':'form-control'}),
            'stock_contity':forms.TextInput(attrs={'class':'form-control'}),
            'discriptions':forms.Textarea(attrs={'class':'form-control'}),
            'worrenty':forms.TextInput(attrs={'class':'form-control'}),
            'return_policy':forms.TextInput(attrs={'class':'form-control'}),
            
            

        }

