from django.urls import path
# from rest_framework.authtoken.view import obtain_auth_token
from .views import CategoryView, ProductView, OrderView, CartProductView, CartView



urlpatterns = [
    # path('auth/', include('djoser.urls')),
    # path('auth/token', obtain_auth_token, name='token')
    path('categorys/', CategoryView.as_view({'get': 'list'})),
    path('products/', ProductView.as_view({'post': 'create'})),
    path('orders/', ProductView.as_view({'post': 'create'})),
]
