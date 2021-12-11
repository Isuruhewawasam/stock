
from django.urls import path
from.views import IndexView,AdminRegisterView,AdminloginView,AdminlogoutView,AddCatergoryView,addproductView,ProductDetailsView,updateproductView,deleteView,Search_kew_word

urlpatterns = [
## app urls
    path('',IndexView.as_view(),name='home'),
    path('add-catergory',AddCatergoryView.as_view(),name='add_catergory'),
    path('add-product',addproductView.as_view(),name='add_product'),
    path('product-details/<slug:slug>/',ProductDetailsView.as_view(),name='product_details'),
    path('update-product/<slug:slug>/',updateproductView.as_view(),name='update_product'),
    path('delete-product/<slug:slug>/',deleteView.as_view(),name='delete_product'),
    path('search/',Search_kew_word.as_view(),name='search'),

## admin urls
    path('admin-register/',AdminRegisterView.as_view(),name='admin_register'),
    path('admin-login/',AdminloginView.as_view(),name='admin_login'),
    path('admin-logout/',AdminlogoutView.as_view(),name='admin_logout'),

]
