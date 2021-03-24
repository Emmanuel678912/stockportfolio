from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), # you need to pass the page for the app, the view and then name it
    path('about.html', views.about, name='about'), # make sure to pass the template page not the actual path 
    path('add_stock.html', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name="delete"),
    path('delete_stock.html', views.delete_stock, name="delete_stock"),

]
