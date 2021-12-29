from django.urls import path
from . import views


urlpatterns = [
    path('addlaptop/',views.addLaptopView.as_view(),name='add'),
    path('showlaptop/',views.showLaptopView,name='show'),
    path('update/<int:id>/',views.updateView,name='update'),
    path('delete/<int:id>/',views.deleteView,name='delete'),
    path('details/<int:id>/',views.details,name='details')
]