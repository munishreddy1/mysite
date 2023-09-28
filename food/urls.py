from . import views 
from django.urls import path

app_name = 'food'
urlpatterns = [
    #/food/
    path('', views.IndexClassView.as_view(), name='index'),
    #/food/1
    path('<int:pk>',views.DetailsClassView.as_view(),name='detail'),
    path('item/', views.item, name='item'),
    #add item 
    path('add', views.CreateClassView.as_view(), name='create_item'),
    path('update/<int:id>/', views.update_item, name='update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]