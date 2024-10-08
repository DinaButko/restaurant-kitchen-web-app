from django.urls import path
from . import views


urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),# when the user visit home page, MenuList will load html file
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item")
]