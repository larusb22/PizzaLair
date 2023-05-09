from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='menu-index'),
    path('<int:id>', views.get_product_by_id, name='product-details')
]