from django.urls import path
from . import views

urlpatterns=[
    path("",views.home, name="home"),
    path('manager/dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('menu/update/<int:menu_id>/', views.update_menu, name='update_menu'),
    path('menu/delete/<int:menu_id>/', views.delete_menu, name='delete_menu'),
]

