from django.urls import path
from.import views
app_name='ecomapp'

urlpatterns = [
    path('', views.AllProdCat, name='AllProdCat'),
    path('<slug:c_slug>/', views.AllProdCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdDetail, name='prodcatdetail'),
]